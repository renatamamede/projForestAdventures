from code.constantes import ENTITY_SPEED
from code.entity import Entity


class EnemyAtk(Entity):

    def __init__(self, name: str, position: tuple, enemy_width: int):
        super().__init__(name, position)
        self.rect.x -= enemy_width

    # Se for tiro:
    def move(self):
        self.rect.x -= ENTITY_SPEED[self.name]