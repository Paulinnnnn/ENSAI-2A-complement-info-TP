from abstract_pokemon import AbstractPokemon


class AllRounder(AbstractPokemon):
    def __init__(self):
        super().__init__()

    def get_pokemon_attack_coef(self):
        return 1 + (self.sp_atk_current + self.sp_def_current) / 200
