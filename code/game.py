# Importações
import pygame
from code.menu import Menu

# Construtor
class Game:
    def __init__(self):
        pygame.init()  # Inicia a execução do pygame
        self.window = pygame.display.set_mode(size=(600,480))  #Cria a janela do jogo com tamanho 600x400px. Se ficar só essa linha, a janela vai abrir e fechar. Temos que fazer com que se mantenha aberta.

    def run(self):
        while True:  # Se deixarmos só esse laço sem nada, a janela não responderá.
            menu = Menu(self.window)
            menu.run()

            for event in pygame.event.get():  # Checa eventos relacionados ao pygame.
                if event.type == pygame.QUIT:
                    pygame.quit()  # Faz com que possamos clicar no botão que fecha a janela
                    quit()  # Encerra o pygame