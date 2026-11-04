import numpy as np
import pygame
import numpy

from window import *
from block import *
from config import *

level = np.zeros(204)

def Create_Block(x, y, id):
    screen.blit(Blocks[id].texture, (x * BLOCK_SIZE, y * BLOCK_SIZE))
    level[y * 17 + x] = id
