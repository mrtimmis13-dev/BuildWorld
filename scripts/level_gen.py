import pygame
import random

from window import *
from block import *
from level import *

def generate_level():
    for y in range(0, 12):
        for x in range(0, 17):
            if y <= 6:
                generate_block_data(x, y, air.id)
            elif y > 6:
                generate_block_data(x, y, grass.id)

def generate():
    for y in range(0, 12):
        for x in range(0, 17):
            create_block(x, y, level[y * 17 + x])