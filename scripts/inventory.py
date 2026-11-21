import pygame

from item_slot import *
from main import *

current_slot = 1
inventory_slots = [1, 2, 3, 4, 5, 6]
inventory_y = [0, 0, 0, 0, 0]

def inventory_draw():
    global current_slot
    inventory = pygame.Surface((500, 80))
    inventory.fill((110, 110, 118))
    inventory.set_alpha(200)

    current_slot_line = pygame.Surface((64, 10))
    current_slot_line.fill((200, 0, 0))

    #text = pygame.font.SysFont("comicsans", 30)
    #texts = text.render(str(current_slot), True, (0, 0, 0))
    #screen.blit(texts, (50, 50))

    screen.blit(inventory, (WIDTH_SCREEN - 780, (HEIGHT_SCREEN - 90)))

    for i in range(1, len(inventory_slots)):
        slot(i, i - 1, inventory_y[i - 1] * 15)
        screen.blit(current_slot_line, ((WIDTH_SCREEN - 770) + ((current_slot - 1) * 80), HEIGHT_SCREEN - 25))

def set_slot(item):
    global current_slot
    global inventory_y
    current_slot = item
    for i in range(0, len(inventory_y)):
        inventory_y[i] = 0
    inventory_y[item - 1] = 1

def get_slot():
    return current_slot