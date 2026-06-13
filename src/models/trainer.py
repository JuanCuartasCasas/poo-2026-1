from typing import List
from .pokemon import Pokemon


class Trainer:
    def __init__(self, nombre: str, team: str, pokemon: List[Pokemon]):

        self.nombre = nombre
        self.team = team
        self.pokemon = pokemon if pokemon is not None else []

    def add_pokemon(self, pokemon: Pokemon):

        if len(self.pokemon) < 6 and pokemon not in self.pokemon:
            self.pokemon.append(pokemon)

        else:
            print("You cannot add more Pokémon or the Pokémon is already in the team.")

    def get_active_pokemon(self):

        if self.pokemon:
            return self.pokemon[0]

        else:
            print("You don't have any Pokémon in your team.")

            return None

    def get_next_available_pokemon_index(self):
        for index, pokemon in enumerate(self.pokemon[1:], start=1):
            if pokemon.stats.hp > 0:
                return index
        return None

    def switch_pokemon(self, pokemon_index):

        if 0 <= pokemon_index < len(self.pokemon):
            self.pokemon[0], self.pokemon[pokemon_index] = (
                self.pokemon[pokemon_index],
                self.pokemon[0],
            )

        else:
            print("Invalid Pokémon index.")

    def handle_evolution(self, old_pokemon, new_pokemon):
        for i, p in enumerate(self.pokemon):
            if p == old_pokemon:
                self.pokemon[i] = new_pokemon
