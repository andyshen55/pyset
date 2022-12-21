import pygame
from pygame import display


# Sets display window size to full screen
def set_game_window():
    display.init()
    infoObject = display.Info()
    display.set_mode((infoObject.current_w, infoObject.current_h))


def game_loop():
    set_game_window()
    running = True

    while running:
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False


if __name__ == "__main__":
    game_loop()
