import pygame
from window import *

def main():
    pygame.init()

    Set_Window("BuildWorld","recources/assets/textures/icon.png", 1080,720)

    pygame.display.update()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()

main()