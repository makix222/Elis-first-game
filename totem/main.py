import pygame as py
from pygame.locals import QUIT
import totem.world.globals as world_values
from totem.pieces.form import PieceManager

py.init()

size_x = 500
size_y = 800
screen_size = size_x, size_y

main_screen = py.display.set_mode(screen_size)
main_clock = py.time.Clock()

done = False
while not done:
    for event in py.event.get():
        if event.type == QUIT:
            py.display.quit()
            py.quit()
    current_screen = py.display.get_surface()
    current_screen.fill(world_values.background_color)
    piece = PieceManager()
    piece.spawn_star(current_screen, (100, 100), 5)
    py.display.flip()
