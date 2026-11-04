import pygame
from window import *
from block import *
from level import *

def Generate():
    for y in range(0, 17):
        for x in range(0, 17):
            Create_Block(x, y, grass.id)