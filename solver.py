from utils import shape_basis, color_basis, number_basis, fill_basis


def is_set(a, b, c):
    shape = (shape_basis[a.shape] + shape_basis[b.shape] + shape_basis[c.shape]) % 3
    color = (color_basis[a.color] + color_basis[b.color] + color_basis[c.color]) % 3
    number = (
        number_basis[a.number] + number_basis[b.number] + number_basis[c.number]
    ) % 3
    fill = (fill_basis[a.fill] + fill_basis[b.fill] + fill_basis[c.fill]) % 3

    if shape == color == number == fill == 0:
        return True

    return False


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
