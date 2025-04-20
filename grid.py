import pygame
from word import RandomWord

class Grid:
    def __init__(self):
        self.num_cols = 5
        self.num_rows = 6
        self.grid_size = 70
        self.grid = [[0 for i in range(self.num_cols)] for j in range(self.num_rows)]
        self.typed_letters = [["" for i in range(self.num_cols)] for j in range(self.num_rows)]
        self.current_col = 0
        self.current_row = 0
    

    def draw_grid_squares(self):
        squares = []
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                rect = pygame.Rect(column*self.grid_size+450, row*self.grid_size+260, self.grid_size-5, self.grid_size-5)
                squares.append(rect)
        return squares
                
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

        
                
