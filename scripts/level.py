import numpy as np
import pygame
import numpy

from scripts import block
from window import *
from block import *
from config import *
from level_gen import *

level = np.zeros(204)

def generate_block_data(x, y, block_id):
    level[y * 17 + x] = block_id

def create_block(x, y, block_id):
    screen.blit(Blocks[block_id].texture, (x * BLOCK_SIZE, y * BLOCK_SIZE))

def set_block(x, y, block_id):
    level[y * 17 + x] = block_id

def get_block(x, y):
    return level[y * 17 + x].tolist()

def save_world():
    level_save = ";".join(map(str, level.astype(int)))
    file = open("saves/level_save.txt", "w")
    file.write(level_save)
    file.close()


def load_world():
    with open('saves/level_save.txt', 'r') as file:
        content = file.read()
        if is_world_empty():
            level_load = content.split(";")
            return level_load

def is_world_empty():
    with open('saves/level_save.txt', 'r') as file:
        content = file.read()
        if content != "":
            return True
    return False