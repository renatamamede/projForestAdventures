# Essa é a nossa classe ABC (abstrata) e terá implementações nas classes filhas
# Importações:
from abc import ABC, abstractmethod
import pygame.image
from code.constantes import ENTITY_HEALTH, ENTITY_DAMAGE, ENTITY_SCORE

# Construtor:
class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./asset/' + name + '.png')#.convert_alpha()  # O Convert_alpha trata as imagens png de uma forma otimizada
        self.rect = self.surf.get_rect(left=position[0], top=position[1])  # Aqui, as posições vêm da tupla, pois as imagens (dos inimigos, por exemplo) poderão surgir de qq lugar da tela
        self.speed = 0  # Será redefinido depois em cada classe
        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name]
        self.score = ENTITY_SCORE[self.name]
        self.last_dmg = 'None'  # Essa entidade vai servir pra calcularmos o score

    @abstractmethod
    def move(self):  # Será implementado pelos filhos da classe, mas o python precisa ser avisado (por isso o decorator @)
        pass
