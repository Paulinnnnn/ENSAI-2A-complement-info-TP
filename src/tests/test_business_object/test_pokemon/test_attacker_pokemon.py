from business_object.pokemon.Attacker import Attacker
from business_object.statistic import Statistic


class TestAttackerPokemon:
    def test_get_coef_damage_type(self):
        # GIVEN
        snorlax = Attacker(stat_current=Statistic(attack=200, speed=200))

        # WHEN
        multiplier = snorlax.get_pokemon_attack_coef()

        # THEN
        assert multiplier == 3


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
