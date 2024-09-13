from business_object.pokemon.AllRounder import AllRounder
from business_object.statistic import Statistic


class AllRounderPokemon:
    def test_get_coef_damage_type(self):
        # GIVEN
        snorlax = AllRounder(stat_current=Statistic(sp_atk=200, sp_def=200))

        # WHEN
        multiplier = snorlax.get_pokemon_attack_coef()

        # THEN
        assert multiplier == 3


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
