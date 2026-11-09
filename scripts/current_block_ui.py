import pygame

from window import *
from block import *
from config import *

def ui(block_id):
    screen.blit(Blocks[block_id].texture, (WIDTH_SCREEN - 75, 20))