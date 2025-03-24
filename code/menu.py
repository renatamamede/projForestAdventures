#Importações
import pygame.image
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface
from code.constantes import WIN_WIDTH, COR_VERMELHO, MENU_OPTION, COR_BRANCO, COR_LARANJA


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/menu.png').convert_alpha()  # Carrega a imagem (mas não coloca ela em lugar nenhum ainda)
        self.rect = self.surf.get_rect(left=0, top=0)  # Esses valores são o padrão (nem precisariam ser explicitados). Significa que o retângulo começa na posição 0 da esquerda e do topo

    def run(self, ):
        menu_option = 0  # Traz, por padrão, a primeira opção do menu selecionada
        pygame.mixer_music.load('./asset/menu.wav')  # Carrega a música do menu
        pygame.mixer_music.play(-1)  # Coloca a música para tocar. O parâmetro '-1' é para fazer a música recomeçar quando acabar.
        while True:
            # Esse código abaixo desenha a imagem (da fonte) no retângulo (destino).
            self.window.blit(source=self.surf,dest=self.rect)  # Essa função blit é do SURFace. Ela que vai "atualizar" a imagem, para colocá-la no lugar.

            # Abaixo vamos colocar os textos do menu
            self.menu_text(80, "FOREST", COR_VERMELHO, ((WIN_WIDTH/2), 100))
            self.menu_text(80, "ADVENTURES", COR_VERMELHO, ((WIN_WIDTH / 2), 200))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], COR_LARANJA, ((WIN_WIDTH / 2), 300 + 30 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], COR_BRANCO, ((WIN_WIDTH / 2),  300+30*i))  # Adiciona o texto do MENU

            # Agora precisamos mostrar de fato a imagem, usando o display, que é o que efetivamente mexe na tela do jogo. Usaremos o metodo FLIP, que atualiza a tela.
            pygame.display.flip()  # É esse aqui que vai fazer aparecer a imagem na janelinha.


            #Checagem e laços de TODOS OS EVENTOS
            for event in pygame.event.get():  # Checa eventos relacionados ao pygame.
                # Evento para fechar a janela:
                if event.type == pygame.QUIT:
                    pygame.quit()  # Faz com que possamos clicar no botão que fecha a janela
                    quit()  # Encerra o pygame

                #Eventos de teclas pressionadas:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION)-1:
                            menu_option +=1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:
                        if len(MENU_OPTION) > menu_option > 0:
                            menu_option -=1
                        else:
                            menu_option = 4
                    if event.key == pygame.K_RETURN: # Tecla Enter
                        return MENU_OPTION[menu_option]



    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):  # Configuração dos textos
        #text_font: Font = pygame.font.SysFont(name='Ink Free', size=text_size) # Aqui, podemos por uma das fontes do sistema
        text_font: Font = pygame.font.Font('./asset/PressStart2P-Regular.ttf', size=text_size)  # Aqui, podemos baixar uma fonte, trazê-la ao projeto e usá-la
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()  # Faz com que os textos virem imagens para aparecer na tela.
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)