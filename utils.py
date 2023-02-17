shapes = ["squiggle", "oval", "diamond"]
colors = ["green", "red", "purple"]
numbers = [1, 2, 3]
fills = ["filled", "blank", "lined"]

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


shape_basis = {"oval": 0, "diamond": 1, "squiggle": 2}
color_basis = {"red": 0, "purple": 1, "green": 2}
number_basis = {1: 0, 2: 1, 3: 2}
fill_basis = {"filled": 0, "blank": 1, "lined": 2}


OFF_WHITE = (250, 250, 250)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

COLS = 7
ROWS = 3
