import pygame
from word import RandomWord

pygame.font.init()
FONT = pygame.font.SysFont("arial", 48)

class Grid:
    def __init__(self):
        self.num_cols = 5
        self.num_rows = 6
        self.grid_size = 70
        self.grid = [[0 for i in range(self.num_cols)] for j in range(self.num_rows)]
        self.typed_letters = [["" for i in range(self.num_cols)] for j in range(self.num_rows)]
        self.current_col = 0
        self.current_row = 0
    

    
    '''
    Draws the actual grid on the screen as well as displaying the letter in each individual box in the grid
    text_rect holds the object of the rectange. It will be displayed as <rect(x, y, w, h)> Pygame takes care of the width and height and will display it perfectly in the center
    '''

    def draw_grid_squares(self, surface):
        squares = []
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                rect = pygame.Rect(column*self.grid_size+450, row*self.grid_size+260, self.grid_size-5, self.grid_size-5)
                squares.append(rect)

                letter = self.typed_letters[row][column]

                if letter:
                    text = FONT.render(letter, True, (255, 255, 255))
                    text_rect = text.get_rect(center=rect.center)
                    surface.blit(text, text_rect)

        return squares
    

    '''
      Replaces every empty string with a letter in the row:
      Takes care of backspace feature
      If the current index in the self.current_col == 5, it means we are at the end of the row, and we need to set current_row to the next row and current_col back to 0 to restart
      on the next row
    '''

    def replace_l_event(self, event):
        if event.type == pygame.KEYDOWN:
            letter = event.unicode.upper()
        if letter.isalpha() and len(letter) == 1:
            if self.current_col < 5:
                self.typed_letters[self.current_row][self.current_col] = letter
                self.current_col += 1

                if self.current_col == 5:
                    self.current_row += 1
                    self.current_col = 0
        if event.key ==  pygame.K_BACKSPACE:
            if self.current_col > 0:
                self.current_col -= 1
                self.typed_letters[self.current_row][self.current_col] = ""


        
                
