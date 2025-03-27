# Importações
import pygame
from pygame import display
from code.constantes import WIN_HEIGHT, WIN_WIDTH, MENU_OPTION
from code.level import Level
from code.menu import Menu
from code.score import Score


# Construtor
class Game:
    def __init__(self):
        pygame.init()  # Inicia a execução do pygame
        self.window = pygame.display.set_mode(size=(WIN_WIDTH,WIN_HEIGHT))  #Cria a janela do jogo com tamanho 600x400px (isso foi antes de fazer as constantes). Se ficar só essa linha, a janela vai abrir e fechar. Temos que fazer com que se mantenha aberta.

    def run(self):
        while True:  # Se deixarmos só esse laço sem nada, a janela não responderá.
            score = Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:  # Opções NEW GAME porque todos vão para a primeira fase
                player_score = [0, 0]  # O score deve ficar instanciado ao jogo, não ao player, senão vai zerar a cada fase. [0, 0] os zeros referem-se a cada jogador. Se for só 1p, mexemos só no primeiro e se forem 2p, mexemos nos 2
                level = Level(self.window, 'Level1', menu_return, player_score)  # O que vai diferenciar o modo de jogo será essa linha
                level_return = level.run(player_score)  # Chama a fase
                if level_return:  # vamos checar pra chamar o segundo lvl
                    level = Level(self.window, 'Level2', menu_return, player_score)  # O que vai diferenciar o modo de jogo será essa linha
                    level_return = level.run(player_score)
                    if level_return:  # Agora, depois, e somente depois da fase 2, vamos pegar o score
                        score.save(menu_return, player_score)

            elif menu_return == MENU_OPTION[3]:  # Opção SCORE
                score.show()

            elif menu_return == MENU_OPTION[4]:  # Opção EXIT
                pygame.quit()
                quit()
            else:
                pass

