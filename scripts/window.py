import pygame

from config import *

screen = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))

def set_window(title, icon):
    pygame.display.set_caption(title)
    pygame.display.set_icon(pygame.image.load(icon))

def get_mouse_pos_x():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    return mouse_x // BLOCK_SIZE

def get_mouse_pos_y():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    return mouse_y // BLOCK_SIZE