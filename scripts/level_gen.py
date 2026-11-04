import pygame
from window import *
from block import *
from level import *

def Generate():
    for y in range(0, 12):
        for x in range(0, 17):
            if y > 6:
                Create_Block(x, y, air.id)
            elif y > 6:
                Create_Block(x, y, grass.id)