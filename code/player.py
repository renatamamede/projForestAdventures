# Importações:
import pygame

from code.constantes import ENTITY_SPEED, WIN_WIDTH, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT
from code.entity import Entity


# Construtor:

class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):  # O ponto 0,0 no plano cartesiano do movimento está no canto superior esquerdo da tela.
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 150:  # Coloquei valores aqui e no K_DOWN para limitar o espaço em que o personagem vai se mover. Não quero que ande além do "caminho".
            self.rect.centery -= ENTITY_SPEED[self.name]  # O player é movimentado mexendo no RECT dele
        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < 485:  # Use IF. Se for ELIF, o jogo vai entender que só pode se pressionar uma tecla de caa vez. Não é a ideia aqui.
             self.rect.centery += ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
             self.rect.centerx += ENTITY_SPEED[self.name]
        pass
