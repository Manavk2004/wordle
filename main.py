import pygame 
import sys

pygame.init()


SCREEN = pygame.display.set_mode((1200, 1000), pygame.RESIZABLE)
width, height = SCREEN.get_size()

player_rect = pygame.Rect(150, 150, 50, 50)
pygame.draw.rect(SCREEN, (255, 0, 0), player_rect)

pygame.display.set_caption("Wordle")
pygame

clock = pygame.time.Clock()
MIN_WIDTH = 800
MIN_HEIGHT = 600

while True:
    player_rect = pygame.Rect(150, 150, 50, 50)
    pygame.draw.rect(SCREEN, (255, 0, 0), player_rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.VIDEORESIZE:
            SCREEN = pygame.display.set_mode(event.size, pygame.RESIZABLE)
            width, height = SCREEN.get_size()
    
        if event.type == pygame.VIDEORESIZE:
            new_width = max(event.w, MIN_WIDTH)
            new_height = max(event.h, MIN_HEIGHT)

            SCREEN = pygame.display.set_mode((new_width, new_height), pygame.RESIZABLE)

    pygame.display.update()
    clock.tick(60)

