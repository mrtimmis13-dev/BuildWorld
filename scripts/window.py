import pygame

from config import *

screen = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))

def Set_Window(title, icon):
    pygame.display.set_caption(title)
    pygame.display.set_icon(pygame.image.load(icon))

