from ..models.stats import Stats
from ..models.move import Move

CHARMANDER_STATS = Stats(hp=20, attack=2, defense=0.3, special_attack=1, special_defense=1, speed=2)

CHARMANDER_STATS_MAX = Stats(
    hp=28, attack=3.5, defense=0.5, special_attack=2, special_defense=2, speed=3.5
)

BULBASAUR_STATS = Stats(hp=20, attack=1, defense=0.3, special_attack=1, special_defense=1, speed=1)

BULBASAUR_STATS_MAX = Stats(
    hp=45, attack=3, defense=0.7, special_attack=4, special_defense=3.5, speed=2.5
)

SQUIRTLE_STATS = Stats(hp=20, attack=1, defense=0.5, special_attack=1, special_defense=1, speed=1)

SQUIRTLE_STATS_MAX = Stats(
    hp=44, attack=3, defense=0.9, special_attack=3, special_defense=3.5, speed=2.5
)

FLAME_BURST = Move(name="Flame Burst", type="Fire", power=5, accuracy=100, pp=25)

VINE_WHIP = Move(name="Vine Whip", type="Grass", power=5, accuracy=100, pp=25)

WATER_GUN = Move(name="Water Gun", type="Water", power=5, accuracy=100, pp=25)
