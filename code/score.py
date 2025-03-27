from datetime import datetime

import pygame
from pygame.constants import KEYDOWN, K_RETURN, K_BACKSPACE, K_ESCAPE
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.DBProxy import DBProxy
from code.constantes import SCORE_POS, COR_LARANJA, MENU_OPTION, COR_BRANCO, COR_VERMELHO


class Score:

    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./asset/score_bg.png').convert_alpha()  # Carrega a imagem (mas não coloca ela em lugar nenhum ainda)
        self.rect = self.surf.get_rect(left=0, top=0)

    def save(self, game_mode: str, player_score: list[int]):
        pygame.mixer_music.load('./asset/score.wav')  # Carrega a música
        pygame.mixer_music.play(-1)  # Dá play e repete quando terminar
        db_proxy = DBProxy('DBScore')  # Conecta ao DB
        name = ''

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(48,'YOU WIN!', COR_LARANJA, SCORE_POS['Title'])
            text = 'Enter Player 1 name:'
            score = player_score[0]
            if game_mode == MENU_OPTION[0]:
                score = player_score[0]
                text = 'Enter Player 1 name: '
            if game_mode == MENU_OPTION[1]:  # PVE
                score = (player_score[0] + player_score[1]) / 2
                text = 'Enter Team name: '
            if game_mode == MENU_OPTION[2]:
                if player_score[0] > player_score[1]:  # Checagem de qual jogador fez mais pontos
                    score = player_score[0]
                    text = 'Enter Player 1 name: '
                if player_score[0] < player_score[1]:
                    score = player_score[1]
                    text = 'Enter Player 2 name: '
                else:
                    score = player_score[0]
                    text = 'It is a Tie! Enter both players initials: '

            self.score_text(20, text, COR_BRANCO, SCORE_POS['EnterName'])


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and len(name) == 3:  # Se for ENTER, vai salvar o score
                        db_proxy.save({'name': name, 'score': score, 'date': get_formatted_date()})
                        self.show()
                        return
                    elif event.key == K_BACKSPACE:  # Se for BACKSPACE, vai apagar
                        name = name[:-1]
                    else:  # AKA: a pessoa vai digitar algo
                        if len(name) < 3:
                            name += event.unicode

            self.score_text(20, name, COR_BRANCO, SCORE_POS['Name'])


            pygame.display.flip()

    def show(self):
        pygame.mixer_music.load('./asset/score.wav')  # Carrega a música
        pygame.mixer_music.play(-1)  # Dá play e repete quando terminar
        self.window.blit(source=self.surf, dest=self.rect)
        self.score_text(48, 'TOP 10 SCORES', COR_LARANJA, SCORE_POS['Title'])
        self.score_text(20, 'NAME     SCORE     DATE', COR_BRANCO, SCORE_POS['Label'])
        self.score_text(20, 'Press [ESC] to go back to the MENU', COR_BRANCO, SCORE_POS['Tutorial'])
        db_proxy = DBProxy('DBScore')  # Conectar ao DB
        list_score = db_proxy.retrieve_top10()  # Traz a lkista dos scores
        db_proxy.close()

        # Agora vamos imprimir linha por linha dos scores:
        for player_score in list_score:
            id_,name,score, date = player_score
            self.score_text(20, f'   {name}      {score :05d}   {date}', COR_BRANCO, SCORE_POS[list_score.index(player_score)])

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
            pygame.display.flip()


    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):  # Configuração dos textos
        text_font: Font = pygame.font.Font('./asset/PressStart2P-Regular.ttf', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()  # Faz com que os textos virem imagens para aparecer na tela.
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

def get_formatted_date():  # É uma função solta dentro do score, não deve ficar indentada dentro da classe mesmo
    current_datetime = datetime.now()
    #current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%y")
    #return f"{current_time} - {current_date}"
    return f"{current_date}"