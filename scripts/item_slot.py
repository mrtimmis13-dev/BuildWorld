import pygame

from window import *
from block import *
from config import *

def slot(block_id, x):
    screen.blit(Blocks[block_id].texture, ((WIDTH_SCREEN - 770) + (x * 80), HEIGHT_SCREEN - 85))