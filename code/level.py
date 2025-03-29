# Importações
import random
import sys
import pygame.display
import pygame.mixer_music
import pygame.time
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface
from code.constantes import COR_BRANCO, WIN_HEIGHT, MENU_OPTION, EVENT_ENEMY, SPAWN_TIME, COR_VERDE, COR_CIANO, \
    EVENT_TIMEOUT, TIMEOUT_STEP, TIMEOUT_LEVEL
from code.enemy import Enemy
from code.entityFactory import EntityFactory
from code.entity import Entity
from code.entityMediator import EntityMediator
from code.player import Player


# Construtor
class Level:
    def __init__(self, window: Surface, name: str, game_mode: str, player_score: list[int]):
        self.timeout = TIMEOUT_LEVEL  # 30 segundos
        self.window = window
        self.name = name
        self.game_mode = game_mode  # Modo de jogo
        self.entity_list: list[Entity] = []  # Lista de entidades vazias
        self.entity_list.extend(EntityFactory.get_entity(self.name.lower() + '_bg'))
        #self.entity_list.extend(EntityFactory.get_entity('lvl1_bg'))  # Vamos trazer a lista dos BGs. Use dessa forma pra ficar mais genérico e trazer sempre que houver a string 'bg' no nome do arquivo.
        player = EntityFactory.get_entity('Player1')  # Inicializar o jogador junto com o BG
        player.score = player_score[0]
        self.entity_list.append(player)
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:  # Se a opção do menu selecionada for a de 2P, vamos gerar o Player 2
            player = EntityFactory.get_entity('Player2')
            player.score = player_score[1]  # Não esquecer que o score do 2P é na posição [1] da lista: [0, 0]
            self.entity_list.append(player)
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)  # Aqui, dizemos qual a taxa de spawn dos inimigos em milissegundos.
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)  # Evento pra checar a condição de vitória da fase.


    def run(self, player_score: list[int]):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)  # Isso aqui é o tanto de FPS que vai executar o jogo
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)  # Desenha as imagens na tela
                ent.move()
                if isinstance(ent, (Player, Enemy)):
                    atk = ent.atk()
                    if atk is not None:
                        self.entity_list.append(atk)
                if ent.name == 'Player1':
                    self.level_text(14, f'Player1 - Health: {ent.health} | Score: {ent.score}', COR_VERDE, (10, 25))
                if ent.name == 'Player2':
                    self.level_text(14, f'Player2 - Health: {ent.health} | Score: {ent.score}', COR_CIANO, (10, 45))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()  # Funciona igual ao quit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))
                    # self.entity_list.append(EntityFactory.get_entity('Enemy1'))  # Pode ser assim, ou como acima pra spawnar mais inimigos diferentes
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP  # Aqui estamos pegando aquele tempo de 20s e tirando 0.1s
                    if self.timeout == 0:
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == 'Player1':
                                player_score[0] = ent.score
                            if isinstance(ent, Player) and ent.name == 'Player2':
                                player_score[1] = ent.score

                        return True  #  Isso acontecendo, vai chamar o próximo level lá no game.py (linha 22 aproximadamente)

                found_player = False  # Vamos buscar o jogador pra ver se ele morreu na fase, pra interromper a execução e dar game over
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        found_player  = True
                if not found_player:  # Ou seja: if found_player == False
                    return False  # Retornando False, a fase termina, e volta pro menu (ou exibe tela de game over)

            # Textos da tela da fase

            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', COR_BRANCO, (10,5))
            #self.level_text(14, f'FPS: {clock.get_fps() :.0f}', COR_BRANCO, (10, WIN_HEIGHT-35))
            #self.level_text(14, f'Entidades: {len(self.entity_list)}', COR_BRANCO, (10, WIN_HEIGHT-20))
            pygame.display.flip()

            #Aqui vamos por o mediador pra verificar colisões e vida das entidades:
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.Font('./asset/PressStart2P-Regular.ttf', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
