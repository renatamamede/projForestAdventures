# Importações
import pygame
from pygame import display
from code.constantes import WIN_HEIGHT, WIN_WIDTH, MENU_OPTION
from code.level import Level
from code.menu import Menu

# Construtor
class Game:
    def __init__(self):
        pygame.init()  # Inicia a execução do pygame
        self.window = pygame.display.set_mode(size=(WIN_WIDTH,WIN_HEIGHT))  #Cria a janela do jogo com tamanho 600x400px (isso foi antes de fazer as constantes). Se ficar só essa linha, a janela vai abrir e fechar. Temos que fazer com que se mantenha aberta.

    def run(self):
        while True:  # Se deixarmos só esse laço sem nada, a janela não responderá.
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:  # Opções NEW GAME porque todos vão para a primeira fase
                level = Level(self.window, 'Level1', menu_return)  # O que vai diferenciar o modo de jogo será essa linha
                level_return = level.run()  # Chama a fase
            elif menu_return == MENU_OPTION[4]:  # Opção EXIT
                pygame.quit()
                quit()
            else:
                pass

