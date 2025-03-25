# Importações
from code.constantes import ENTITY_SPEED, WIN_WIDTH, ENTITY_ATK_DELAY
from code.enemyAtk import EnemyAtk
from code.entity import Entity

# Construtor
class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.atk_delay = ENTITY_ATK_DELAY[self.name]

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def atk(self):
        self.atk_delay -= 1
        if self.atk_delay == 0:
            self.atk_delay = ENTITY_ATK_DELAY[self.name]
            return EnemyAtk(name=f'{self.name}Atk', position=(self.rect.centerx, self.rect.centery))

