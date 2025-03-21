# Importações
import pygame.display
from code.entityFactory import EntityFactory
from code.entity import Entity

# Construtor
class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode  # Modo de jogo
        self.entity_list: list[Entity] = []  # Lista de entidades vazias
        self.entity_list.extend(EntityFactory.get_entity('lvl1_bg'))  # Vamos trazer a lista dos BGs

    def run(self, ):
        while True:
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)  # Desenha as imagens na tela
                ent.move()
            pygame.display.flip()
