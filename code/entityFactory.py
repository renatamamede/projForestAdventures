import random
from code.background import Background
from code.constantes import WIN_WIDTH, WIN_HEIGHT
from code.enemy import Enemy
from code.player import Player


class EntityFactory:
    # Essa classe nunca terá um __init__, pois ela nunca instancia, só invoca outros objetos que serão instanciados
    # def __init__(self):
    #    pass

    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'level1_bg':  # Nome dos bg. Carregue todos em uma lista
                list_bg = []
                for i in range(4):  # Aqui, optei por tirar a última camada (que tem uns matinhos e umas pedras) pra ficar mais bonitinho. Tava muito feio com essa última.
                    list_bg.append(Background(f'lvl1_bg{i}', (0, 0)))
                    list_bg.append(Background(f'lvl1_bg{i}', (WIN_WIDTH,0)))  # Precisamos fazer isso para ir repetindo as imagens conforme as anteriores saem da tela
                    # Agora precisamos fazer essas 10 imagens rodarem infinitamente. Veja no background.py como é feito.
                return list_bg
            case 'level2_bg':  # Nome dos bg. Carregue todos em uma lista
                list_bg = []
                for i in range(4):
                    list_bg.append(Background(f'lvl2_bg{i}', (0, 0)))
                    list_bg.append(Background(f'lvl2_bg{i}', (WIN_WIDTH, 0)))  # Precisamos fazer isso para ir repetindo as imagens conforme as anteriores saem da tela
                    # Agora precisamos fazer essas 10 imagens rodarem infinitamente. Veja no background.py como é feito.
                return list_bg
            case 'Player1':
                return Player('Player1', (10, WIN_HEIGHT / 2 - 40))  # Essas posições são onde "nasce" a entidade
            case 'Player2':
                return Player('Player2', (10, WIN_HEIGHT / 2 + 40))
            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(200, 450)))
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(200, 450)))
