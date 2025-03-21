from code.background import Background
from code.constantes import WIN_WIDTH


class EntityFactory:
    # Essa classe nunca terá um __init__, pois ela nunca instancia, só invoca outros objetos que serão instanciados
    #def __init__(self):
    #    pass

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):  # 0,0 é o padrão
        match entity_name:
            case 'lvl1_bg':  # Nome dos bg. Carregue todos em uma lista
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'lvl1_bg{i}', (0,0)))
                    list_bg.append(Background(f'lvl1_bg{i}', (WIN_WIDTH,0)))  # Precisamos fazer isso para ir repetindo as imagens conforme as anteriores saem da tela
                    #Agora precisamos fazer essas 10 imagens rodarem infinitamente. Veja no background.py como é feito.

                return list_bg

