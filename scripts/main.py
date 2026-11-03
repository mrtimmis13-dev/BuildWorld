import pygame

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
        Create_Block(1, 1, grass.id)
        Create_Block(2, 1, grass.id)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()


if __name__ == "__main__":
    main()