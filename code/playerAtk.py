from code.constantes import ENTITY_SPEED
from code.entity import Entity


class PlayerAtk(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)


    # Se for tiro:
    def move(self):
        self.rect.centerx += ENTITY_SPEED[self.name]
