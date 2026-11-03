import pygame

from scripts import block
from window import *
from block import *

def main():
    pygame.init()

    Set_Window("BuildWorld","recources/assets/textures/icon.png")

    running = True
    while running:

        screen.blit(blocks.texture, (0, 0))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()

main()