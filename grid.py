import pygame

class Grid:
    def __init__(self):
        self.num_cols = 5
        self.num_rows = 6
        self.grid_size = 70
        self.grid = [[0 for i in range(self.num_cols)] for j in range(self.num_rows)]
    

    def draw_grid_squares(self):
        squares = []
        for column in range(self.num_cols):
            for row in range(self.num_rows):
                rect = pygame.Rect(column*self.grid_size+450, row*self.grid_size+260, self.grid_size-5, self.grid_size-5)
                squares.append(rect)
        return squares
                
                
