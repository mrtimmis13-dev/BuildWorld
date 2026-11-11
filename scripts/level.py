import numpy as np
import pygame
import numpy

from scripts import block
from window import *
from block import *
from config import *

level = np.zeros(408)

def generate_block_data(x, y, block_id):
    level[y * 17 + x] = block_id

def create_block(x, y, block_id):
    screen.blit(Blocks[block_id].texture, (x * BLOCK_SIZE, y * BLOCK_SIZE))

def set_block(x, y, block_id):
    level[y * 17 + x] = block_id
    print(level[y * 17 + x])

def get_block(x, y):
    return level[y * 17 + x].tolist()
