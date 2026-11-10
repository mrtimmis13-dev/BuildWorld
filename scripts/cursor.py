import pygame

from window import *
from block import *
from config import *

def cursor():
    screen.blit(pygame.transform.scale(pygame.image.load("recources/assets/textures/cursor.png"), (BLOCK_SIZE, BLOCK_SIZE)), (get_mouse_pos_x() * BLOCK_SIZE, get_mouse_pos_y() * BLOCK_SIZE))