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
        color = BLACK if grid.used_keys.get(letter) else GRAY
        pygame.draw.rect(SCREEN, color, rect)
    
        # Render the letter text
        text_surface = FONT.render(letter, True, WHITE)
        text_rect = text_surface.get_rect(center=rect.center)
        SCREEN.blit(text_surface, text_rect)

    
    for letter, rect in key.draw_line2(SCREEN):
        color = BLACK if  grid.used_keys.get(letter) else GRAY
        pygame.draw.rect(SCREEN, color, rect)
        # Render the letter text
        text_surface = FONT.render(letter, True, WHITE)
        text_rect = text_surface.get_rect(center=rect.center)
        SCREEN.blit(text_surface, text_rect)



    for letter, rect in key.draw_line3(SCREEN):
        color = BLACK if  grid.used_keys.get(letter) else GRAY
        pygame.draw.rect(SCREEN, color, rect)
        # Render the letter text
        text_surface = FONT.render(letter, True, WHITE)
        text_rect = text_surface.get_rect(center=rect.center)
        SCREEN.blit(text_surface, text_rect)

                



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
   
        if event.type == pygame.KEYDOWN:
            grid.replace_l_event(event, SCREEN)

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            key_buttons = key.draw_line1(SCREEN) + key.draw_line2(SCREEN) + key.draw_line3(SCREEN)

            for letter, rect in key_buttons:
                if rect.collidepoint(mouse_pos):
                    if grid.current_col < 5:
                        grid.typed_letters[grid.current_row][grid.current_col] = letter
                        grid.word.append(letter)
                        grid.current_col += 1
                    break  # Prevent inserting multiple letters
            
    grid.draw_grid_squares(SCREEN)
    pygame.display.update()
    clock.tick(60)