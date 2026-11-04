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

    running = True
    while running:

        #screen.blit(grass.texture, (0, 0))
        Generate()
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
                    print(mouse.get_pos())
                elif event.button == 3:
                    print(2)


if __name__ == "__main__":
    main()