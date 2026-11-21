
from level_gen import *
from level import *
from cursor import *
from inventory import *

def main():

    pygame.init()

    set_window("BuildWorld","recources/assets/textures/icon.png")

    generate_level()

    running = True

    while running:

        screen.fill((120, 165, 207))
        generate()
        cursor()

        inventory_draw()

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_world()
                running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    save_world()
                    running = False
                    pygame.quit()
                if event.key == pygame.K_1:
                    set_slot(1)
                elif event.key == pygame.K_2:
                    set_slot(2)
                elif event.key == pygame.K_3:
                    set_slot(3)
                elif event.key == pygame.K_4:
                    set_slot(4)
                elif event.key == pygame.K_5:
                    set_slot(5)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if get_block(get_mouse_pos_x(), get_mouse_pos_y()) == 0:
                        set_block(get_mouse_pos_x(), get_mouse_pos_y(), inventory_slots[current_slot - 1])
                elif event.button == 3:
                    set_block(get_mouse_pos_x(), get_mouse_pos_y(), 0)
                elif event.button == 2:
                    if get_block(get_mouse_pos_x(), get_mouse_pos_y()) != 0:
                     current_block = get_block(get_mouse_pos_x(), get_mouse_pos_y())

if __name__ == "__main__":
    main()