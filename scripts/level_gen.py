import pygame
from window import *
from block import *
from level import *

def Generate():
    for x in range(0, 34):
        Create_Block(x, 15, grass.id)