import random
from typing import TYPE_CHECKING, List

from .type_relations import TypeRelations
from ..models.move import Move

if TYPE_CHECKING:
    from ..models.pokemon import Pokemon


class CombatEngine:
    @staticmethod
    def hit_accuracy(attack: Move, defender_types: List[str]):

        tp = TypeRelations()

        effect = tp.get_effectiveness(attack.type, defender_types)

        factor = random.random()

        return (attack.accuracy > (factor * effect) / (factor + 1), effect)

    @staticmethod
    def calculate_damage(attacker: "Pokemon", defender: "Pokemon", move: Move):

        att_stats = attacker.stats
        def_stats = defender.stats

        is_able_to_attack, multiplier = CombatEngine.hit_accuracy(move, defender.types)

        rlevel = attacker.level / defender.level

        rdef = att_stats.attack / def_stats.defense

        damage = int(is_able_to_attack) * (rlevel * rdef * multiplier * move.power)

        print(f"Damage: {damage}")

        return damage
