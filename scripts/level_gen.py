
from level import *
from main import *

def generate_level():
    if not is_world_empty():
        for y in range(0, 12):
            for x in range(0, 17):
                if y <= 6:
                    generate_block_data(x, y, air.id)
                elif y == 7:
                    generate_block_data(x, y, grass.id)
                elif y == 8 or y == 9 or y == 10:
                    generate_block_data(x, y, dirt.id)
                elif y == 11 or y == 12:
                    generate_block_data(x, y, stone.id)
    else:
        a = load_world()
        for y in range(0, 12):
            for x in range(0, 17):
                generate_block_data(x, y, a[y * 17 + x])

def generate():
    for y in range(0, 12):
        for x in range(0, 17):
            create_block(x, y, level[y * 17 + x])

def level_zero():
    if is_world_empty():
        global level
        level = np.zeros(204)