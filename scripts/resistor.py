def resistor(colour: str) -> int:
    bands = ["black", "brown", "red", "orange", "yellow",
             "green", "blue", "violet", "grey", "white"]
    colours = colour.split("-")
    value = str(bands.index(colours[0])) + str(bands.index(colours[1]))
    return int(value)


"""
value += str(bands.index(colour)) for colour in colours[:2]
"""
