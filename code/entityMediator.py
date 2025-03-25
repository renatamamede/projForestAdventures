# Essa classe irá gerenciar as colisões, ataques e etc
from code.constantes import WIN_WIDTH
from code.enemy import Enemy
from code.enemyAtk import EnemyAtk
from code.entity import Entity
from code.playerAtk import PlayerAtk


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):  # verificar diversas colisões, incluindo quando ele sair da tela pra ser destruído e não ficar ocupando espaço. As duas underlines no metodo significam que ela é privada e só vai funcionar dentro dessa classe.
        if isinstance(ent, Enemy):  # Verifica apenas inimigos, já que o player e o background não precisam ser destruídos
            if ent.rect.right <= 0:
                ent.health = 0
        if isinstance(ent, PlayerAtk):
            if ent.rect.left > WIN_WIDTH:
                ent.health = 0
        if isinstance(ent, EnemyAtk):
            if ent.rect.right <= 0:
                ent.health = 0

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            test_entity = entity_list[i]
            EntityMediator.__verify_collision_window(test_entity)

    @staticmethod
    def verify_health(entity_list: list[Entity]):  # Checa a vida da entidade. Se for 0, ela morre (é destruída)
        for ent in entity_list:
            if ent.health<=0:
                entity_list.remove(ent)