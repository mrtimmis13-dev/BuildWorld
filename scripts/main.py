import pygame
from pygame import mouse

from scripts import block
from window import *
from block import *
from level_gen import *
from level import *
from current_block_ui import *

def main():
    pygame.init()

    set_window("BuildWorld","recources/assets/textures/icon.png")

    generate_level()

    gen = True
    running = True
    current_block = 1

    while running:

        screen.fill((120, 165, 207))
        generate()
        ui(current_block)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()
                if event.key == pygame.K_1:
                    current_block = 1
                elif event.key == pygame.K_2:
                    current_block = 2
                elif event.key == pygame.K_3:
                    current_block = 3

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    set_block(get_mouse_pos_x(), get_mouse_pos_y(), current_block)
                elif event.button == 3:
                    set_block(get_mouse_pos_x(), get_mouse_pos_y(), 0)

if __name__ == "__main__":
    main()