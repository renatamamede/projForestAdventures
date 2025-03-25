# Aqui ficarão os valores constantes que usamos várias vezes, sem ter que ficar mudando manualmente nas classes.
import pygame

#C
COR_VERMELHO = (237, 24, 24)
COR_BRANCO = (255,255,255)
COR_LARANJA = (255,150,40)

#E
ENTITY_ATK_DELAY = {
'Player1': 5,
'Player2': 5,
'Enemy1': 20,
'Enemy2': 20,
}

ENTITY_HEALTH = {
    'lvl1_bg0': 999,
    'lvl1_bg1': 999,
    'lvl1_bg2': 999,
    'lvl1_bg3': 999,
    'lvl1_bg4': 999,
    'Player1': 300,
    'Player1Atk': 1,
    'Player2': 300,
    'Player2Atk': 1,
    'Enemy1': 50,
    'Enemy1Atk': 1,
    'Enemy2': 80,
    'Enemy2Atk': 1,
}

ENTITY_SPEED = {
    'lvl1_bg0': 3,
    'lvl1_bg1': 3,
    'lvl1_bg2': 2,
    'lvl1_bg3': 3,
    'lvl1_bg4': 7,
    'Player1': 10,
    'Player1Atk': 10,
    'Player2': 10,
    'Player2Atk': 10,
    'Enemy1': 7,
    'Enemy1Atk': 10,
    'Enemy2': 5,
    'Enemy2Atk': 12,
}

EVENT_ENEMY = pygame.USEREVENT + 1

#M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - PVE',
               'NEW GAME 2P - PVP',
               'SCORE',
               'EXIT')

#P
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                 'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                 'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                 'Player2': pygame.K_d}
PLAYER_KEY_ATK = {'Player1': pygame.K_RCTRL,
                 'Player2': pygame.K_LCTRL}

#S
SPAWN_TIME = 1000

#W
WIN_WIDTH = 960  # Largura da janela do jogo
WIN_HEIGHT = 540  # Altura da janela do jogo