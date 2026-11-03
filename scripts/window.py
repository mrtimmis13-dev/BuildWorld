import pygame

def Set_Window(title, icon, weight_screen, height_screen):
    screen = pygame.display.set_mode((weight_screen, height_screen))
    pygame.display.set_caption(title)
    pygame.display.set_icon(pygame.image.load(icon))

    screen.fill((120, 165, 207))