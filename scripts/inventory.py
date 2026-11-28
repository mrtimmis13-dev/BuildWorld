
from item_slot import *
from main import *

current_slot = 1
current_line = 1
inventory_slots = [2, 2, 3, 1, 5]
inventory_y = [0, 0, 0, 0, 0]

def inventory_draw():
    global current_slot
    inventory = pygame.Surface((500, 80))
    inventory.fill((110, 110, 118))
    inventory.set_alpha(200)

    current_slot_line = pygame.Surface((64, 10))
    current_slot_line.fill((200, 0, 0))

    screen.blit(inventory, (WIDTH_SCREEN - 780, (HEIGHT_SCREEN - 90)))

    for i in range(1, len(inventory_slots) + 1):
        slot(inventory_slots[i - 1], i - 1, inventory_y[i - 1] * 15)
        screen.blit(current_slot_line, ((WIDTH_SCREEN - 770) + ((current_line - 1) * 80), HEIGHT_SCREEN - 25))

def set_slot(slot):
    global inventory_slots
    global current_line
    global current_slot
    global inventory_y
    current_line = slot
    current_slot = inventory_slots[slot - 1]
    for i in range(0, len(inventory_y)):
        inventory_y[i] = 0
    inventory_y[slot - 1] = 1

def get_slot():
    return current_slot

def get_slot_item(i):
    print(inventory_slots[i])
    return inventory_slots[i]