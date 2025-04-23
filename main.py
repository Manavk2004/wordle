import pygame 
import sys
from grid import *
from colors import *
from keyboard_handler import Letter

pygame.init()

FONT = pygame.font.SysFont(None, 40)  # You can tweak the size


grid = Grid()
grid.got_word()
key = Letter()

SCREEN = pygame.display.set_mode((1200, 900))
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
    
    for letter, rect in key.draw_line1(SCREEN):
        pygame.draw.rect(SCREEN, GRAY, rect)
    
        # Render the letter text
        text_surface = FONT.render(letter, True, WHITE)
        text_rect = text_surface.get_rect(center=rect.center)
        SCREEN.blit(text_surface, text_rect)

    
    for letter, rect in key.draw_line2(SCREEN):
        pygame.draw.rect(SCREEN, GRAY, rect)
    
        # Render the letter text
        text_surface = FONT.render(letter, True, WHITE)
        text_rect = text_surface.get_rect(center=rect.center)
        SCREEN.blit(text_surface, text_rect)

        

    for letter, rect in key.draw_line3(SCREEN):
        pygame.draw.rect(SCREEN, GRAY, rect)
    
        # Render the letter text
        text_surface = FONT.render(letter, True, WHITE)
        text_rect = text_surface.get_rect(center=rect.center)
        SCREEN.blit(text_surface, text_rect)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
   
        if event.type == pygame.KEYDOWN:
            grid.replace_l_event(event, SCREEN)
            
    grid.draw_grid_squares(SCREEN)
    pygame.display.update()
    clock.tick(60)