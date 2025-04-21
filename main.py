import pygame 
import sys
from grid import *
from colors import *

pygame.init()


grid = Grid()

SCREEN = pygame.display.set_mode((1200, 1000))
width, height = SCREEN.get_size()

pygame.display.set_caption("Wordle")

clock = pygame.time.Clock()
MIN_WIDTH = 800
MIN_HEIGHT = 600

while True:
    SCREEN.fill(BLACK)
    for square in grid.draw_grid_squares(SCREEN):
        pygame.draw.rect(SCREEN, GRAY, square)
        inset_rect = square.inflate(-2, -2)
        pygame.draw.rect(SCREEN, BLACK, inset_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
   
        if event.type == pygame.KEYDOWN:
            grid.replace_l_event(event)
    grid.draw_grid_squares(SCREEN)
    pygame.display.update()
    clock.tick(60)