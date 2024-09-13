from abstract_pokemon import AbstractPokemon


class Defender(AbstractPokemon):
    def __init__(self):
        super().__init__()

    def get_pokemon_attack_coef(self):
        return 1 + (self.attack_current + self.defense_current) / 200
