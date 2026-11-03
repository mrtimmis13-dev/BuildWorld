import pygame

screen = pygame.display.set_mode((1080, 720))

def Set_Window(title, icon):
    pygame.display.set_caption(title)
    pygame.display.set_icon(pygame.image.load(icon))
    screen.fill((120, 165, 207))
