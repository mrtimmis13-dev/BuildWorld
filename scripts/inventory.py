import pygame

from scripts.window import screen
from config import *
from item_slot import *
from main import *

current_slot = 1
inventory_slots = [1, 2, 3, 4, 5, 6]


def inventory_draw():
    global current_slot
    inventory = pygame.Surface((500, 80))
    inventory.fill((110, 110, 118))
    inventory.set_alpha(200)

    current_slot_line = pygame.Surface((64, 10))
    current_slot_line.fill((200, 0, 0))

    screen.blit(inventory, (WIDTH_SCREEN - 780, HEIGHT_SCREEN - 90))
    #screen.blit(current_slot_line, ((WIDTH_SCREEN - 770) + (1 * 80), HEIGHT_SCREEN - 25))

    for i in range(1, len(inventory_slots)):
        slot(i, i - 1)
        screen.blit(current_slot_line, ((WIDTH_SCREEN - 770) + ((current_slot - 1) * 80), HEIGHT_SCREEN - 25))
        print(current_slot)

def set_slot(item):
    global current_slot
    current_slot = item