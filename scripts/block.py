import pygame

class Block:
    def __init__(self, name, texture, id):
        square = pygame.Surface((32, 32))
        square.fill((0, 255, 0))
        self.texture = pygame.image.load(texture)
        self.id = id

grass = Block("Grass", "recources/assets/textures/blocks/grass.png", 1)
dirt = Block("Dirt", "recources/assets/textures/blocks/grass.png", 2)
stone = Block("Stone", "recources/assets/textures/blocks/grass.png", 3)

Blocks = {

    grass.id: grass,
    dirt.id: dirt,
    stone.id: stone

}