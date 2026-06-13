from __future__ import annotations

from typing import List
import copy

from .move import Move, Moveset
from .stats import Stats
from ..engine.combat_engine import CombatEngine
from ..engine.type_relations import TypeRelations


class Pokemon:
    def __init__(
        self,
        name: str,
        types: List[str],
        stats: Stats,
        stats_max: Stats | None = None,
        level: int = 1,
        moveset: Moveset | None = None,
        evolution: str | None = None,
        evolution_level: int | None = None,
    ) -> None:

        self.name = name
        self.types = types
        self.stats = stats
        self.level = level

        self.experience = 0

        self.experience_to_level_up = self.level * 10

        self.moveset = moveset if moveset else Moveset()

        self.evolution = evolution
        self.evolution_level = evolution_level
        self.stats_max = stats_max if stats_max else stats
        self.stats_base = copy.copy(stats)

    def get_stats(self) -> str:
        return f"{self.name} Estadísticas: {self.stats}"

    def attack(self, target: "Pokemon", move: Move, relations: TypeRelations) -> "Pokemon" | None:

        damage = CombatEngine.calculate_damage(self, target, move)

        print(f"{self.name} attacks {target.name} with {move.name}")

        was_alive = not target.is_fainted()

        target.defender(damage)

        if was_alive and target.is_fainted():
            print(f"\n{target.name} was defeated!")

            exp_gained = target.level * 5

            if target.level > self.level:
                exp_gained = int(exp_gained * 1.5)

                print("Bonus experience for defeating a stronger opponent!")

            return self.gain_experience(exp_gained)
        else:
            return None

    def gain_experience(self, amount: int) -> "Pokemon" | None:

        self.experience += amount

        print(f"{self.name} gained {amount} experience points.")

        print(f"EXP current: {self.experience}/{self.experience_to_level_up}")

        return self.level_up()

    def level_up(self) -> "Pokemon" | None:

        while self.experience >= self.experience_to_level_up:
            self.experience -= self.experience_to_level_up

            self.level += 1

            self.experience_to_level_up = self.level * 10

            self.stats.attack = self.stats_base.attack + (self.level - 1) / 99 * (
                self.stats_max.attack - self.stats_base.attack
            )

            self.stats.defense = self.stats_base.defense + (self.level - 1) / 99 * (
                self.stats_max.defense - self.stats_base.defense
            )

            self.stats.special_attack = self.stats_base.special_attack + (self.level - 1) / 99 * (
                self.stats_max.special_attack - self.stats_base.special_attack
            )

            self.stats.special_defense = self.stats_base.special_defense + (self.level - 1) / 99 * (
                self.stats_max.special_defense - self.stats_base.special_defense
            )

            self.stats.speed = self.stats_base.speed + (self.level - 1) / 99 * (
                self.stats_max.speed - self.stats_base.speed
            )

            self.stats.hp = self.stats_base.hp + (self.level - 1) / 99 * (
                self.stats_max.hp - self.stats_base.hp
            )

            new = self.evolve()

            if new:
                print(
                    f"\n{new.name} evolved to level {new.level}\n"
                    f"--New Statistics:--\n"
                    f"HP: {new.stats.hp}\n"
                    f"Attack: {new.stats.attack}\n"
                    f"Defense: {new.stats.defense}\n"
                    f"Special Attack: {new.stats.special_attack}\n"
                    f"Special Defense: {new.stats.special_defense}\n"
                    f"Speed: {new.stats.speed}\n"
                    f"EXP necessary for the next level: {new.experience_to_level_up}"
                )
                return new
            else:
                print(f"\n{self.name} leveled up to {self.level}!")

                print(
                    f"\nNew Statistics:"
                    f"\nHP: {self.stats.hp}"
                    f"\nAttack: {self.stats.attack}"
                    f"\nDefense: {self.stats.defense}"
                    f"\nSpecial Attack: {self.stats.special_attack}"
                    f"\nSpecial Defense: {self.stats.special_defense}"
                    f"\nSpeed: {self.stats.speed}"
                )

                print(f"\nEXP necessary for the next level: {self.experience_to_level_up}")
        return None

    def defender(self, damage: float) -> None:
        damage_received = damage * (1 - self.stats.defense)
        self.stats.hp = self.stats.hp - damage_received

        if self.stats.hp <= 0:
            self.stats.hp = 0

        print(f"{self.name} received {damage_received:.2f} damage")

        print(f"Remaining life: {self.stats.hp:.2f}")

    def is_fainted(self) -> bool:
        return self.stats.hp <= 0

    def evolve(self):

        if (
            self.evolution is not None
            and self.evolution_level is not None
            and self.level >= self.evolution_level
        ):
            old_name = self.name

            print(f"{old_name} is evolving...")

            if self.evolution == "Charmeleon":
                new_pokemon = Charmeleon(level=self.level)
                new_pokemon.moveset = self.moveset
                new_pokemon.experience = self.experience
                new_pokemon.experience_to_level_up = self.experience_to_level_up
                print(f"{old_name} evolved into {new_pokemon.name}!")
                return new_pokemon

        return None


class Charmeleon(Pokemon):
    def __init__(self, level):
        super().__init__(
            name="Charmeleon",
            types=["Fire"],
            stats=Stats(
                hp=30,
                attack=4,
                defense=0.5,
                special_attack=2,
                special_defense=2,
                speed=2,
            ),
            stats_max=Stats(
                hp=58,
                attack=7,
                defense=0.8,
                special_attack=4,
                special_defense=4,
                speed=4,
            ),
        )
