# Aqui ficarão os valores constantes que usamos várias vezes, sem ter que ficar mudando manualmente nas classes.
import pygame

#C
COR_VERMELHO = (237, 24, 24)
COR_BRANCO = (255,255,255)
COR_LARANJA = (255,150,40)
COR_VERDE = (155,254,141)
COR_CIANO = (255,128,255)

#E
ENTITY_ATK_DELAY = {
'Player1': 5,
'Player2': 5,
'Enemy1': 20,
'Enemy2': 20,
}

ENTITY_DAMAGE = {
    'lvl1_bg0': 0,
    'lvl1_bg1': 0,
    'lvl1_bg2': 0,
    'lvl1_bg3': 0,
    'lvl1_bg4': 0,
    'lvl2_bg0': 0,
    'lvl2_bg1': 0,
    'lvl2_bg2': 0,
    'lvl2_bg3': 0,
    'lvl2_bg4': 0,
    'Player1': 1,
    'Player1Atk': 20,
    'Player2': 1,
    'Player2Atk': 20,
    'Enemy1': 50,
    'Enemy1Atk': 30,
    'Enemy2': 80,
    'Enemy2Atk': 30,
}

ENTITY_HEALTH = {
    'lvl1_bg0': 999,
    'lvl1_bg1': 999,
    'lvl1_bg2': 999,
    'lvl1_bg3': 999,
    'lvl1_bg4': 999,
    'lvl2_bg0': 999,
    'lvl2_bg1': 999,
    'lvl2_bg2': 999,
    'lvl2_bg3': 999,
    'lvl2_bg4': 999,
    'Player1': 300,
    'Player1Atk': 1,
    'Player2': 300,
    'Player2Atk': 1,
    'Enemy1': 50,
    'Enemy1Atk': 1,
    'Enemy2': 80,
    'Enemy2Atk': 1,
}

ENTITY_SCORE = {
    'lvl1_bg0': 0,
    'lvl1_bg1': 0,
    'lvl1_bg2': 0,
    'lvl1_bg3': 0,
    'lvl1_bg4': 0,
    'lvl2_bg0': 0,
    'lvl2_bg1': 0,
    'lvl2_bg2': 0,
    'lvl2_bg3': 0,
    'lvl2_bg4': 0,
    'Player1': 0,
    'Player1Atk': 0,
    'Player2': 0,
    'Player2Atk': 0,
    'Enemy1': 100,
    'Enemy1Atk': 0,
    'Enemy2': 200,
    'Enemy2Atk': 0,
}

ENTITY_SPEED = {
    'lvl1_bg0': 3,
    'lvl1_bg1': 3,
    'lvl1_bg2': 2,
    'lvl1_bg3': 3,
    'lvl1_bg4': 7,
    'lvl2_bg0': 3,
    'lvl2_bg1': 3,
    'lvl2_bg2': 2,
    'lvl2_bg3': 3,
    'lvl2_bg4': 7,
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

EVENT_TIMEOUT = pygame.USEREVENT +2

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

#T
TIMEOUT_STEP = 100  # Para diminuir o tempo de duração das fases
TIMEOUT_LEVEL = 10000

#W
WIN_WIDTH = 960  # Largura da janela do jogo
WIN_HEIGHT = 540  # Altura da janela do jogo

# Temos que deixar esse Score aqui pra poder identificar o wn_width (tem q ser depois que já definimos ele)
SCORE_POS = {
    'Title': (WIN_WIDTH / 2, 50),
    'EnterName': (WIN_WIDTH / 2, 100),
    'Label': (WIN_WIDTH / 2, 110),
    'Name': (WIN_WIDTH / 2, 130),
    'Tutorial': (WIN_WIDTH / 2, 500),
    0: (WIN_WIDTH / 2, 140),
    1: (WIN_WIDTH / 2, 160),
    2: (WIN_WIDTH / 2, 180),
    3: (WIN_WIDTH / 2, 200),
    4: (WIN_WIDTH / 2, 220),
    5: (WIN_WIDTH / 2, 240),
    6: (WIN_WIDTH / 2, 260),
    7: (WIN_WIDTH / 2, 280),
    8: (WIN_WIDTH / 2, 300),
    9: (WIN_WIDTH / 2, 320),
}