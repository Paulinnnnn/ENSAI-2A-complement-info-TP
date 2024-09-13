from business_object.pokemon.abstract_pokemon import AbstractPokemon


class Attacker(AbstractPokemon):
    def __init__(self, stat_max=None, stat_current=None, level=0, name=None, type_pk=None):
        super().__init__()

    def get_pokemon_attack_coef(self):
        return 1 + (self.speed_current + self.attack_current) / 200
