# Essa classe irá gerenciar as colisões, ataques e etc
from code.constantes import WIN_WIDTH
from code.enemy import Enemy
from code.enemyAtk import EnemyAtk
from code.entity import Entity
from code.player import Player
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
    def __verify_collision_entity(ent1, ent2):  # queremos colisões apenas entre Player x Enemy.
        valid_interaction = False
        if isinstance(ent1, Enemy) and isinstance(ent2, PlayerAtk):
            valid_interaction = True
        elif isinstance(ent1, PlayerAtk) and isinstance(ent2, Enemy):
            valid_interaction = True
        elif isinstance(ent1, EnemyAtk) and isinstance(ent2, Player):
            valid_interaction = True
        elif isinstance(ent1, Player) and isinstance(ent2, EnemyAtk):
            valid_interaction = True

        # Se a interação é valida (True), haverá a COLISÃO. É aqui que colocamos aquelas quatro perguntas que validam ou não a colisão.
        if valid_interaction:  # if valid_interaction == True:
            if (ent1.rect.right >= ent2.rect.left and
                    ent1.rect.left <= ent2.rect.right and
                    ent1.rect.bottom >= ent2.rect.top and
                    ent1.rect.top <= ent2.rect.bottom):
                ent1.health -= ent2.damage
                ent2.health -= ent1.damage
                ent1.last_dmg = ent2.name  # Para calcular o score, vamos ver quem deu o ultimo dano na entidade
                ent2.last_dmg = ent1.name

    @staticmethod
    def __give_score(enemy: Enemy, entity_list: list[Entity]):
        if enemy.last_dmg == 'Player1Atk':
            for ent in entity_list:
                if ent.name == 'Player1':
                    ent.score += enemy.score
        elif enemy.last_dmg == 'Player2Atk':
            for ent in entity_list:
                if ent.name == 'Player2':
                    ent.score += enemy.score

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i+1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    def verify_health(entity_list: list[Entity]):  # Checa a vida da entidade. Se for 0, ela morre (é destruída)
        for ent in entity_list:
            if ent.health<=0:
                if isinstance(ent,Enemy):
                    EntityMediator.__give_score(ent, entity_list)
                entity_list.remove(ent)