from scripts.resistor import resistor


def test_resistor_returns_15_2_colours_passed():
    assert resistor("brown-green") == 15
