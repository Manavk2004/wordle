import pygame 
import sys
from grid import Grid

pygame.init()

Grid = Grid()

SCREEN = pygame.display.set_mode((1200, 1000))
width, height = SCREEN.get_size()

pygame.display.set_caption("Wordle")

clock = pygame.time.Clock()
MIN_WIDTH = 800
MIN_HEIGHT = 600

while True:
    for square in Grid.draw_grid_squares():
        pygame.draw.rect(SCREEN, (0, 0, 0), square)
        inset_rect = square.inflate(-2, -2)
        pygame.draw.rect(SCREEN, (128, 128, 128), inset_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(60)
