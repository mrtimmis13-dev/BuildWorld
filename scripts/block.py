import pygame

class Block:
    def __init__(self, name, texture):
        square = pygame.Surface((32, 32))
        square.fill((0, 255, 0))
        self.texture = pygame.image.load(texture)

grass = Block("Grass", "recources/assets/textures/blocks/grass.png")
dirt = Block("Dirt", "recources/assets/textures/blocks/grass.png")
stone = Block("Stone", "recources/assets/textures/blocks/grass.png")
