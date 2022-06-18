def resistor(colour: str) -> int:
    bands = ["black", "brown", "red", "orange", "yellow",
             "green", "blue", "violet", "grey", "white"]
    colours = colour.split("-")
    return int(str(bands.index(colours[0])) + str(bands.index(colours[1])))


"""
value += str(bands.index(colour)) for colour in colours[:2]
"""
