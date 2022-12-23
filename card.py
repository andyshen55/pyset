from utils import compress_card


class Card:
    def __init__(self, shape, color, number, fill) -> None:
        self.shape = shape.lower()
        self.color = color.lower()
        self.number = number
        self.fill = fill.lower()

    def __repr__(self):
        return f"shape: {self.shape}, color: {self.color}, number: {self.number}, fill: {self.fill}"

    def card_string(self):
        return compress_card(self.shape, self.color, self.number, self.fill)


if __name__ == "__main__":
    shapes = ["squiggle", "oval", "diamond"]
    colors = ["green", "red", "purple"]
    numbers = [1, 2, 3]
    fills = ["filled", "blank", "lined"]

    deck = []
    for s in shapes:
        for c in colors:
            for n in numbers:
                for f in fills:
                    deck.append(Card(s, c, n, f))

    assert len(deck) == pow(3, 4)

    for card in deck:
        compressed = card.card_string()
        print(compressed, card, "", sep="\n")
