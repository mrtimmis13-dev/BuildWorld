import pygame
from window import *
from block  import *

def Create_Block(x, y, id):
    screen.blit(Blocks[id].texture, (x * 64, y * 64))
