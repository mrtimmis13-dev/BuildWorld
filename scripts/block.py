import pygame

from config import *

class Block:
    def __init__(self, name, texture, block_id):
        square = pygame.Surface((32, 32))
        square.fill((0, 255, 0))
        self.texture = pygame.transform.scale(pygame.image.load(texture), (BLOCK_SIZE, BLOCK_SIZE))
        self.id = block_id

air = Block("Air", "recources/assets/textures/blocks/air.png", 0)
grass = Block("Grass", "recources/assets/textures/blocks/grass.png", 1)
dirt = Block("Dirt", "recources/assets/textures/blocks/dirt.png", 2)
stone = Block("Stone", "recources/assets/textures/blocks/stone.png", 3)
planks = Block("Planks", "recources/assets/textures/blocks/cobblestone.png", 4)
cobblestone = Block("Cobblestone", "recources/assets/textures/blocks/planks.png", 5)

Blocks = {

    air.id: air,
    grass.id: grass,
    dirt.id: dirt,
    stone.id: stone,
    planks.id: planks,
    cobblestone.id: cobblestone

}