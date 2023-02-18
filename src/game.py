from card import Card
from solver import is_set, find_sets
from utils import shapes, colors, numbers, fills

from random import seed, shuffle, choice


class Game:
    def __init__(self) -> None:
        seed("set")
        cap_size = 21

        self.deck = self.generate_deck()
        shuffle(self.deck)
        self.cards = self.deck[-cap_size:]
        self.deck = self.deck[:-cap_size]
        self.selected = []

        self.sets = []
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
        else:
            self.selected.remove(card_index)

        if len(self.selected) == 3:
            i, j, k = self.selected
            card1, card2, card3 = self.cards[i], self.cards[j], self.cards[k]

            found = is_set(card1, card2, card3)
            if found:
                self.replace_cards()
                self.sets = []
                self.hint_set = []

            self.selected = []

    def replace_cards(self):
        for card in self.selected:
            self.cards[card] = self.deck.pop()

    """
    Following code would not be provided by students. 
    - Solve function in game class is used for rendering pygame
    - hint indices and play are for text-based debugging
    """

    def solve(self):
        if len(self.sets) == 0:
            self.sets = find_sets(self.cards)

        hint_set = choice(self.sets)
        hint_indices = []

        for index, card in enumerate(self.cards):
            if card in hint_set:
                hint_indices.append(index)

        self.hint_set = hint_indices
