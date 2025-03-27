#Importações:
from code.constantes import WIN_WIDTH, ENTITY_SPEED
from code.entity import Entity

# Construtor:
class Background(Entity):
    def __init__(self, name: str, position: tuple):  # Tava marcando um errinho aqui, foi só adicionar a superclasse que resolveu
        super().__init__(name, position)

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]  # O nùmero é a velocidade. Para a movimentação do fundo, precisamos fazer com que ele se desloque para a esquerda, ou seja, diminuindo o eixo X
        if self.rect.right <= 0:  # Aqui fazemos as imagens se repetirem ao longo da fase
            self.rect.left = WIN_WIDTH  # Se o canto direito da imagem chegar ao canto esquerdo, a imagem é jogada de volta para a direita, gerando o loop infinito de imagens
        pass
