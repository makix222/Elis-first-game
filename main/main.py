import pygame
import main.globals as world_params


pygame.init()

size_x = 500
size_y = 800
screen_size = size_x, size_y

main_screen = pygame.display.set_mode(screen_size)
main_clock = pygame.time.Clock()

done = False
while not done:
    pygame.Surface().fill(world_params.background_color)

