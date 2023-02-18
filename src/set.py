import pygame
from pygame import display
import os
from game import Game

from utils import OFF_WHITE, GREEN, BLUE, COLS, ROWS

# Sets display window size to full screen
def set_game_window():
    display.init()
    infoObject = display.Info()
    win = display.set_mode((infoObject.current_w, infoObject.current_h))
    display.set_caption("Set Solver")
    return win


# Generate asset path for card
def card_to_img(card):
    fill_dict = {"filled": "filled", "lined": "shaded", "blank": "empty"}
    return f"{card.color}{card.shape}{fill_dict[card.fill]}{card.number}.png"


# Dynamically compute card dimensions based on full screen size
def get_card_size(win, card):
    full_w, full_h = win.get_size()

    # Load arbitrary card to set ratios
    card_path = os.path.join("assets", card_to_img(card))
    im_w, im_h = pygame.image.load(card_path).get_size()
    ratio = im_h / im_w

    # Leave two cards as space for vertical gaps
    resized_w = full_w // (COLS + 2)
    resized_h = int(resized_w * ratio)

    return resized_w, resized_h


# Get horizontal/vertical offsets to render card at specified index
def get_wh_offsets(win, card_w, card_h, index):
    full_w, full_h = win.get_size()

    # Constants chosen based on rendered layout, may need to adjust for different screen sizes
    w_gap = card_w // 4
    h_gap = card_h // 2

    board_w = (card_w * COLS) + (w_gap * (COLS - 1))
    board_h = (card_h * ROWS) + (h_gap * (ROWS - 1))

    # Horizontally center board. Leave a third of the vertical space for solve button
    w_offset = (full_w - board_w) // 2
    h_offset = (full_h - board_h) // 3

    row = index // 7
    col = index % 7

    # Card position defined as h/w offset + gap dependent on number of cards before
    im_w_gap = col * (card_w + w_gap)
    im_h_gap = row * (card_h + h_gap)

    return im_w_gap + w_offset, im_h_gap + h_offset


# Render solver button with text, and return Rect positions for main loop to handle clicks
def get_rendered_solve_button(win):
    full_w, full_h = win.get_size()

    # Button size constants chosen purely for aesthetic reasons
    button_w = full_w // 3
    button_h = full_h // 10

    # Offsets depend on chosen button size, need to adjust if changed
    solve_button = (full_w // 3, 2 * (full_h // 3), button_w, button_h)
    pygame.draw.rect(win, BLUE, solve_button, border_radius=25)

    # Text width/height are center-aligned, rather than top left corner
    text_w = full_w // 2
    text_h = solve_button[1] + (solve_button[3] // 2)

    font = pygame.font.Font(None, 69)
    text = font.render("Solve", True, OFF_WHITE)
    textRect = text.get_rect()
    textRect.center = text_w, text_h

    win.blit(text, textRect)

    return solve_button


# Render board and currently selected cards
def draw_window(win, game):
    win.fill(OFF_WHITE)
    resized_w, resized_h = get_card_size(win, game.cards[0])

    for index, card in enumerate(game.cards):
        card_path = os.path.join("assets", card_to_img(card))
        im = pygame.image.load(card_path)
        im = pygame.transform.scale(im, (resized_w, resized_h))

        w_pos, h_pos = get_wh_offsets(win, resized_w, resized_h, index)
        win.blit(im, (w_pos, h_pos))

    get_rendered_solve_button(win)

    for card_index in game.hint_set:
        w_pos, h_pos = get_wh_offsets(win, resized_w, resized_h, card_index)
        rect_dims = (w_pos, h_pos, resized_w, resized_h)

        pygame.draw.rect(win, BLUE, rect_dims, width=4)

    for card_index in game.selected:
        w_pos, h_pos = get_wh_offsets(win, resized_w, resized_h, card_index)
        rect_dims = (w_pos, h_pos, resized_w, resized_h)

        pygame.draw.rect(win, GREEN, rect_dims, width=4)

    display.update()


def game_loop():
    pygame.font.init()
    win = set_game_window()
    game = Game()
    board = []

    button_w, button_h, size_w, size_h = get_rendered_solve_button(win)
    solve_button = pygame.Rect(button_w, button_h, size_w, size_h)

    # Use non-rendered rectangles to represent card clickboxes
    resized_w, resized_h = get_card_size(win, game.cards[0])
    for i in range(21):
        w_pos, h_pos = get_wh_offsets(win, resized_w, resized_h, i)
        board.append(pygame.Rect(w_pos, h_pos, resized_w, resized_h))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                for i in range(21):
                    if board[i].collidepoint(x, y):
                        game.select_card(i)

                if solve_button.collidepoint(x, y):
                    game.solve()

            if event.type == pygame.QUIT:
                running = False

        draw_window(win, game)

    pygame.quit()


if __name__ == "__main__":
    game_loop()
