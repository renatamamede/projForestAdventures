# Importações
import pygame
from code.constantes import WIN_HEIGHT, WIN_WIDTH
from code.menu import Menu

# Construtor
class Game:
    def __init__(self):
        pygame.init()  # Inicia a execução do pygame
        self.window = pygame.display.set_mode(size=(WIN_WIDTH,WIN_HEIGHT))  #Cria a janela do jogo com tamanho 600x400px (isso foi antes de fazer as constantes). Se ficar só essa linha, a janela vai abrir e fechar. Temos que fazer com que se mantenha aberta.

    def run(self):
        while True:  # Se deixarmos só esse laço sem nada, a janela não responderá.
            menu = Menu(self.window)
            menu.run()


