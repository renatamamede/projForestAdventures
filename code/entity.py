# Essa é a nossa classe ABC (abstrata) e terá implementações nas classes filhas
# Importações:
from abc import ABC, abstractmethod
import pygame.image


# Construtor:
class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./asset/' + name + '.png')
        self.rect = self.surf.get_rect(left=position[0], top=position[1])  # Aqui, as posições vêm da tupla, pois as imagens (dos inimigos, por exemplo) poderão surgir de qq lugar da tela
        self.speed = 0  # Será redefinido depois em cada classe

    @abstractmethod
    def move(self, ):  # Será implementado pelos filhos da classe, mas o python precisa ser avisado (por isso o decorator @)
        pass
