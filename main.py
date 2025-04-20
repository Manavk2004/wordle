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
    for square in Grid.draw_grid_squares():
        pygame.draw.rect(SCREEN, GRAY, square)
        inset_rect = square.inflate(-2, -2)
        pygame.draw.rect(SCREEN, BLACK, inset_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
   
        if event.type == pygame.KEYDOWN:
            print(event.unicode)
        

    pygame.display.update()
    clock.tick(60)
