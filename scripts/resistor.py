def resistor(colour: str) -> int:
    bands = ["black", "brown", "red", "orange", "yellow",
             "green", "blue", "violet", "grey", "white"]
    value = ""
    colours = colour.split("-")
    for colour in colours[:2]:
        value += str(bands.index(colour))
    return int(value)
