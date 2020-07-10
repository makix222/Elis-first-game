import pygame as py
import sys
from pygame.locals import *
import totem.world.globals as world_values
from totem.pieces.form import PieceManager
from totem.keyboard.keyboard_manager import KeyManager

py.init()

size_x = 500
size_y = 800
screen_size = size_x, size_y

main_screen = py.display.set_mode(screen_size)
main_clock = py.time.Clock()

keyboard_manager = KeyManager()
piece_manager = PieceManager()

done = False
while not done:
    for event in py.event.get():
        if event.type == QUIT:
            py.display.quit()
            py.quit()
            sys.exit(0)
        if event.type == KEYDOWN:
            keyboard_manager.process_new_keys(py.key.get_pressed())

    current_screen = py.display.get_surface()
    current_screen.fill(world_values.background_color)

    piece_manager.spawn_star(current_screen, (100, 100), 5)
    main_clock.tick(30)
    py.display.flip()

