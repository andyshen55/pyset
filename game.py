from card import Card
from solver import is_set, find_sets
from utils import shapes, colors, numbers, fills

from random import seed, sample, shuffle, choice


class Game:
    def __init__(self) -> None:
        seed(42)
        cap_size = 21

        self.deck = self.generate_deck()
        self.cards = sample(self.deck, cap_size)
        self.selected = []

        self.hint = False
        self.hint_set = []

    def generate_deck(self):
        deck = []
        for s in shapes:
            for c in colors:
                for n in numbers:
                    for f in fills:
                        deck.append(Card(s, c, n, f))

        return deck

    def select_card(self, card_index):
        if card_index not in self.selected:
            self.selected.append(card_index)

        if len(self.selected) == 3:
            i, j, k = self.selected
            card1, card2, card3 = self.cards[i], self.cards[j], self.cards[k]

            found = is_set(card1, card2, card3)
            if found:
                self.replace_cards()
                self.hint = False

            self.selected = []

    def replace_cards(self):
        shuffle(self.deck)
        curr = 0
        replacements = []

        while len(replacements) < 3:
            if self.deck[curr] not in self.cards:
                replacements.append(self.deck[curr])

            curr += 1

        for i, card in enumerate(self.selected):
            self.cards[card] = replacements[i]

    """
    Following code would not be provided by students. 
    - Solve function in game class is used for rendering pygame
    - hint indices and play are for text-based debugging
    """

    def solve(self):
        if not self.hint:
            sets = find_sets(self.cards)
            hint_set = choice(sets)
            self.hint_set = []

            for card in self.cards:
                if card in hint_set:
                    self.hint_set.append(card)

        self.hint = not self.hint

    def get_hint_indices(self):
        indices = {}
        for c in self.hint_set:
            for i, o in enumerate(self.cards):
                if c == o:
                    indices[i] = o
                    break

        return indices

    def play(self):
        while True:
            print("Board")
            for i, card in enumerate(game.cards):
                print(f"{i}: {card}")
            print()

            print("Hint:")
            game.solve()
            for k, v in game.get_hint_indices().items():
                print(f"{k}: {v}")
            print()

            a = input("c1: ")
            b = input("c2: ")
            c = input("c3: ")

            self.select_card(int(a))
            self.select_card(int(b))
            self.select_card(int(c))


if __name__ == "__main__":
    game = Game()
    game.play()
