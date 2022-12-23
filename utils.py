shape_map = {
    "oval": "o",
    "diamond": "d",
    "squiggle": "s",
    "o": "oval",
    "d": "diamond",
    "s": "squiggle",
}

color_map = {
    "red": "r",
    "purple": "p",
    "green": "g",
    "r": "red",
    "p": "purple",
    "g": "green",
}

fill_map = {
    "filled": "f",
    "blank": "b",
    "lined": "l",
    "f": "filled",
    "b": "blank",
    "l": "lined",
}


def compress_card(shape, color, number, fill):
    return f"{shape_map[shape]}{color_map[color]}{number}{fill_map[fill]}"
