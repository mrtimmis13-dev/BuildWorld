import pygame
from pygame import mouse

from scripts import block
from window import *
from block import *
from level_gen import *
from level import *

def main():
    pygame.init()

    Set_Window("BuildWorld","recources/assets/textures/icon.png")

    generate_level()

    gen = True
    running = True
    while running:
        screen.fill((120, 165, 207))

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
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    block_mouse_x, block_mouse_y = mouse_x // BLOCK_SIZE, mouse_y // BLOCK_SIZE
                    set_block(block_mouse_x, block_mouse_y, 0)
                    generate()
                elif event.button == 3:
                    print(2)


if __name__ == "__main__":
    main()