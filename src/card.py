from utils import shape_basis, color_basis, fill_basis


class Card:
    def __init__(self, shape, color, number, fill) -> None:
        self.shape = shape
        self.color = color
        self.number = number
        self.fill = fill

    def __repr__(self):
        shape, color, number, fill = self.convert_bases()
        return f"shape: {shape} | color: {color} | number: {number} | fill: {fill}"

    def __eq__(self, other):
        return (
            self.shape == other.shape
            and self.color == other.color
            and self.number == other.number
            and self.fill == other.fill
        )

    def __add__(self, other):
        shape = (self.shape + other.shape) % 3
        color = (self.color + other.color) % 3
        number = (self.number + other.number) % 3
        fill = (self.fill + other.fill) % 3

        return Card(shape, color, number, fill)

    def convert_bases(self):
        shape = shape_basis[self.shape]
        color = color_basis[self.color]
        number = self.number + 1
        fill = fill_basis[self.fill]

        return shape, color, number, fill
