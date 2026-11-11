import pygame
import random

from window import *
from block import *
from level import *
from main import *

def generate_level():
    for y in range(0, 12):
        for x in range(0, 34):
            if y <= 6:
                generate_block_data(x, y, air.id)
            elif y == 7:
                generate_block_data(x, y, grass.id)
            elif y == 8 or y == 9 or y == 10:
                generate_block_data(x, y, dirt.id)
            elif y == 11 or y == 12:
                generate_block_data(x, y, stone.id)

def generate():
    for y in range(0, 12):
        for x in range(0, 17):
            create_block(x, y, level[y * 17 + x])