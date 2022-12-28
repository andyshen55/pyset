import pygame
from pygame import display
import os
from game import Game


# Sets display window size to full screen
def card_to_img(card):
    fill_dict = {'filled':'filled', 'lined':'shaded', 'blank':'empty'}
    return ''.join((card.color, card.shape, fill_dict[card.fill], str(card.number), '.png'))

def set_game_window():
    display.init()
    infoObject = display.Info()
    win = display.set_mode((infoObject.current_w, infoObject.current_h))
    display.set_caption("Set")
    return win

def draw_window(win, game):
    win.fill((255, 255, 255))
    for index, card in enumerate(game.cards):
        win.blit(pygame.image.load(os.path.join('assets', card_to_img(card))), ((index%7)*200, display.Info().current_h//3 + (index//7)*100))
    for card in game.selected:
        pygame.draw.rect(win, (255, 0, 0), ((card%7)*200, display.Info().current_h//3 + (card//7) * 100, 200, 100), 4)
    display.update()


def game_loop():
    win = set_game_window()
    game = Game()
    board = []
    for i in range(3):
        row = []
        for j in range(7):
            row.append(pygame.Rect(j*200, display.Info().current_h//3 + i*100, 200, 100))
        board.append(row)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                for i in range(3):
                    for j in range(7):
                        if board[i][j].collidepoint(x, y):
                            game.select_card(7*i + j)

            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            
        draw_window(win, game)

    pygame.quit()


if __name__ == "__main__":
    game_loop()
