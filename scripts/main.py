import pygame
from pygame import mouse

from scripts import block
from window import *
from block import *
from level_gen import *
from level import *

def main():
    pygame.init()

    set_window("BuildWorld","recources/assets/textures/icon.png")

    generate_level()

    gen = True
    running = True
    while running:

        generate()

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    set_block(get_mouse_pos_x(), get_mouse_pos_y(), 0)
                elif event.button == 3:
                    set_block(get_mouse_pos_x(), get_mouse_pos_y(), 1)

if __name__ == "__main__":
    main()