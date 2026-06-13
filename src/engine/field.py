import random
import time

from .type_relations import TypeRelations
from ..models.trainer import Trainer


class Field:
    """Implementa el campo de batalla con sus características y efectos.

    Determina el orden del primer turno a partir de la velocidad del Pokémon activo de cada
    entrenador y luego alterna los turnos entre los participantes.
    """

    def __init__(self, trainer1: Trainer, trainer2: Trainer):
        self.trainer1 = trainer1
        self.trainer2 = trainer2

    def determine_turn_order(self):
        pokemon1 = self.trainer1.get_active_pokemon()
        pokemon2 = self.trainer2.get_active_pokemon()

        if pokemon1.stats.speed > pokemon2.stats.speed:
            return [pokemon1, pokemon2]
        elif pokemon2.stats.speed > pokemon1.stats.speed:
            return [pokemon2, pokemon1]
        else:
            # Si la velocidad es igual, se decide al azar
            return list(random.choice([(pokemon1, pokemon2), (pokemon2, pokemon1)]))

    def battle_finished(self, participants):

        for p in participants:
            if p.stats.hp <= 0:
                return True
        return False

    def battlefield(self):
        participants = self.determine_turn_order()
        turn_index = 0
        battle_active = True
        relations = TypeRelations()

        print("\n" + "=" * 60)
        print(f"BATALLA  : {self.trainer1.nombre} vs {self.trainer2.nombre}")
        print("\n" + "=" * 60)

        while battle_active and not self.battle_finished(participants):
            attacker = participants[turn_index]
            defender = participants[1 - turn_index]

            print(
                f"\n TURNO de {attacker.name.upper()} (Velocidad: {attacker.stats.speed}) CONTRA "
                f"{defender.name.upper()} (Velocidad: {defender.stats.speed})"
            )

            print(f"\n Movimientos disponibles para {attacker.name}:")
            for i, move in enumerate(attacker.moveset.get_moves()):
                print(
                    f"[{i + 1}] {move.name} | Tipo: {move.type} | Poder: {move.power}|PP: {move.pp}"
                )

            while True:
                try:
                    choice = (
                        int(
                            input(
                                f"Selecciona el movimiento para {attacker.name}"
                                f" (1-{len(attacker.moveset.get_moves())}): "
                            )
                        )
                        - 1
                    )
                    if 0 <= choice < len(attacker.moveset.get_moves()):
                        break
                    else:
                        raise ValueError("Número fuera de rango.")
                except ValueError as e:
                    print(f"Entrada no válida. {e}")

            movement = attacker.moveset.get_moves()[choice]

            print(f"{attacker.name} usa {movement.name}!")

            evolved = attacker.attack(defender, movement, relations)
            if evolved is not None:
                trainer = self.trainer1 if attacker in self.trainer1.pokemon else self.trainer2
                trainer.handle_evolution(attacker, evolved)
                attacker = evolved
                participants[turn_index] = evolved

            if defender.stats.hp <= 0:
                defender_trainer = (
                    self.trainer1 if defender in self.trainer1.pokemon else self.trainer2
                )
                next_pokemon_index = defender_trainer.get_next_available_pokemon_index()

                if next_pokemon_index is None:
                    print(f"\n¡{defender.name} ha sido derrotado! {attacker.name} gana la batalla.")
                    break

                defender_trainer.switch_pokemon(next_pokemon_index)
                next_defender = defender_trainer.get_active_pokemon()
                participants[1 - turn_index] = next_defender

                print(
                    f"\n{defender_trainer.nombre} envió a {next_defender.name} "
                    f"para continuar la batalla."
                )

            print(f"\n{'=' * 20}")
            print("¿Qué deseas hacer?")
            print("[1] Continuar la batalla")
            print("[2] Cambiar de Pokémon")
            print("[3] Rendirse")
            print(f"{'=' * 20}")
            while True:
                try:
                    decision = int(input("Selecciona una opción (1-3): "))
                    if decision == 1:
                        # Continuar
                        turn_index = 1 - turn_index
                        time.sleep(1)
                        break
                    elif decision == 2:
                        # Cambiar Pokémon
                        trainer = (
                            self.trainer1 if attacker in self.trainer1.pokemon else self.trainer2
                        )
                        print(f"\nPokémon disponibles en el equipo de {trainer.nombre}:")
                        for i, pok in enumerate(trainer.pokemon):
                            print(f"[{i + 1}] {pok.name} (Vida: {pok.stats.hp:.1f})")

                        while True:
                            try:
                                pok_choice = (
                                    int(
                                        input(
                                            "Selecciona Pokémon (1-{}): ".format(
                                                len(trainer.pokemon)
                                            )
                                        )
                                    )
                                    - 1
                                )
                                if 0 <= pok_choice < len(trainer.pokemon):
                                    if trainer.pokemon[pok_choice].stats.hp > 0:
                                        trainer.switch_pokemon(pok_choice)
                                        active_pokemon = trainer.get_active_pokemon()
                                        print(f"¡{trainer.nombre} envió a {active_pokemon.name}!")
                                        participants[turn_index] = active_pokemon

                                        turn_index = 1 - turn_index
                                        time.sleep(1)
                                        break
                                    else:
                                        raise ValueError("Ese Pokémon no puede batallar.")
                                else:
                                    raise ValueError("Índice inválido")
                            except ValueError as e:
                                print(f" {e}")
                        break
                    elif decision == 3:
                        # Rendirse
                        trainer = (
                            self.trainer1 if attacker in self.trainer1.pokemon else self.trainer2
                        )
                        print(f"\n¡{trainer.nombre} se rindió!")
                        battle_active = False
                        break
                    else:
                        raise ValueError("Opción no válida (1-3)")
                except ValueError as e:
                    print(f" {e}")
