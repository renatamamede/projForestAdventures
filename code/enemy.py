# Importações
import pygame

from code.constantes import ENTITY_SPEED, ENTITY_ATK_DELAY
from code.enemyAtk import EnemyAtk
from code.entity import Entity

# Construtor
class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.atk_delay = ENTITY_ATK_DELAY[self.name]

        # ==================================================================================
        # Criar uma lista pra fazer o personagem "andar"
        self.images = [
            pygame.image.load(f'./asset/{name}.png'),
            pygame.image.load(f'./asset/{name}-2.png'),
            pygame.image.load(f'./asset/{name}-3.png'),
            pygame.image.load(f'./asset/{name}-4.png'),
        ]
        self.image_index = 0
        self.surf = self.images[self.image_index]

    # ===================================================================================

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        moved = True
        if moved:
            self.image_index = (self.image_index + 1) % len(self.images)
            self.surf = self.images[self.image_index]

    def atk(self):
        self.atk_delay -= 1
        if self.atk_delay == 0:
            self.atk_delay = ENTITY_ATK_DELAY[self.name]
            return EnemyAtk(name=f'{self.name}Atk', position=(self.rect.centerx, self.rect.centery))

