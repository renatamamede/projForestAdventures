# Importações
import sys
import pygame.display
import pygame.mixer_music
import pygame.time
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.constantes import COR_BRANCO, WIN_HEIGHT
from code.entityFactory import EntityFactory
from code.entity import Entity

# Construtor
class Level:
    def __init__(self, window, name, game_mode):
        self.timeout = 20000  # 20 segundos
        self.window = window
        self.name = name
        self.game_mode = game_mode  # Modo de jogo
        self.entity_list: list[Entity] = []  # Lista de entidades vazias
        self.entity_list.extend(EntityFactory.get_entity('lvl1_bg'))  # Vamos trazer a lista dos BGs

    def run(self):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)  # Isos qui é o tanto de FPS que vai executar o jogo
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)  # Desenha as imagens na tela
                ent.move()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()  # Funciona igual ao quit()

            # Textos da tela da fase
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', COR_BRANCO, (10,5))
            self.level_text(14, f'FPS: {clock.get_fps() :.0f}', COR_BRANCO, (10, WIN_HEIGHT-35))
            self.level_text(14, f'Entidades: {len(self.entity_list)}', COR_BRANCO, (10, WIN_HEIGHT-20))
            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.Font('./asset/PressStart2P-Regular.ttf', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
