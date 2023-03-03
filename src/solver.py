from card import Card


def is_set(a, b, c):
    summed = a + b + c
    return summed == Card(0, 0, 0, 0)


def find_sets(cards):
    sets = []
    n = len(cards)

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                card1, card2, card3 = cards[i], cards[j], cards[k]
                if is_set(card1, card2, card3):
                    sets.append((card1, card2, card3))

    return sets
