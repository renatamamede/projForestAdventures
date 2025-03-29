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
        self.walk = [
            pygame.image.load(f'./asset/{name}.png'),
            pygame.image.load(f'./asset/{name}-2.png'),
            pygame.image.load(f'./asset/{name}-3.png'),
            pygame.image.load(f'./asset/{name}-4.png'),
            pygame.image.load(f'./asset/{name}-5.png'),
            pygame.image.load(f'./asset/{name}-6.png'),
            pygame.image.load(f'./asset/{name}-7.png'),
            pygame.image.load(f'./asset/{name}-8.png'),
        ]
        self.walk_index = 0
        self.surf = self.walk[self.walk_index]

        self.atk_img = [
            pygame.image.load(f'./asset/{name}Atk-1.png'),
            #pygame.image.load(f'./asset/{name}Atk-2.png'),
            #pygame.image.load(f'./asset/{name}Atk-3.png'),
            #pygame.image.load(f'./asset/{name}Atk-4.png'),
            #pygame.image.load(f'./asset/{name}Atk-5.png')
        ]
        self.atk_index = 0
        self.surf = self.atk_img[self.atk_index]

    # ===================================================================================

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        moved = True
        if moved:
            self.walk_index = (self.walk_index + 1) % len(self.walk)
            self.surf = self.walk[self.walk_index]

    def atk(self):
        self.atk_delay -= 1
        if self.atk_delay == 0:
            self.atk_delay = ENTITY_ATK_DELAY[self.name]
            attacking = True
            if attacking:
                self.atk_index = (self.atk_index + 1) % len(self.atk_img)
                self.surf = self.atk_img[self.atk_index]
            return EnemyAtk(name=f'{self.name}Atk', position=(self.rect.x, self.rect.centery), enemy_width=self.rect.width)
