from ..models.move import Moveset
from ..models.pokemon import Pokemon
from ..models.trainer import Trainer
from ..engine.field import Field
from .constants import (
    CHARMANDER_STATS,
    CHARMANDER_STATS_MAX,
    BULBASAUR_STATS,
    BULBASAUR_STATS_MAX,
    SQUIRTLE_STATS,
    SQUIRTLE_STATS_MAX,
    FLAME_BURST,
    VINE_WHIP,
    WATER_GUN,
)


def main() -> None:
    charmander_moveset = Moveset([FLAME_BURST])
    charmander = Pokemon(
        "Charmander",
        ["Fire"],
        CHARMANDER_STATS,
        CHARMANDER_STATS_MAX,
        moveset=charmander_moveset,
        evolution="Charmeleon",
        evolution_level=5,
    )

    bulbasaur_moveset = Moveset([VINE_WHIP])
    bulbasaur = Pokemon(
        "Bulbasaur",
        ["Grass"],
        BULBASAUR_STATS,
        BULBASAUR_STATS_MAX,
        moveset=bulbasaur_moveset,
    )

    squirtle_moveset = Moveset([WATER_GUN])
    squirtle = Pokemon(
        "Squirtle", ["Water"], SQUIRTLE_STATS, SQUIRTLE_STATS_MAX, moveset=squirtle_moveset
    )

    entrenador1 = Trainer("Ash", "Team Rocket", [charmander, bulbasaur])
    entrenador2 = Trainer("Misty", "Team Water", [squirtle])

    campo = Field(entrenador1, entrenador2)
    campo.battlefield()
