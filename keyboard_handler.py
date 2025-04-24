import pygame

class Letter:
    def __init__(self):
        self.keyboard_line1 = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"]
        self.keyboard_line2 = ["A", "S", "D", "F", "G", "H", "J", "K", "L"]
        self.keyboard_line3 = ["Z", "X", "C", "V", "B", "N", "M"]
        self.grid_size = 60
        self.used_keys = {}
    
    def draw_line1(self, surface):
        keys = []
        spacing = self.grid_size + 10
        row_width = spacing * len(self.keyboard_line1)
        start_x = (surface.get_width() - row_width) // 2

        y = surface.get_height() - 4 * (self.grid_size + 20)

        for index, letter in enumerate(self.keyboard_line1):
            rect = pygame.Rect(start_x + index*spacing, y, self.grid_size, self.grid_size)
            keys.append((letter, rect))
        
        return keys

    def draw_line2(self, surface):
        keys = []
        spacing = self.grid_size + 10
        row_width = spacing * len(self.keyboard_line2)
        start_x = (surface.get_width() - row_width) // 2

        y = surface.get_height() - 3*(self.grid_size+20)

        for index, letter in enumerate(self.keyboard_line2):
            rect = pygame.Rect(start_x + index*spacing, y, self.grid_size, self.grid_size)
            keys.append((letter, rect))
        return keys
    
    def draw_line3(self, surface):
        keys = []
        spacing = self.grid_size + 10
        row_width = spacing *len(self.keyboard_line3)
        start_x = (surface.get_width() - row_width) // 2

        y = surface.get_height() - 2*(self.grid_size+20)

        for index, letter in enumerate(self.keyboard_line3):
            rect = pygame.Rect(start_x + index*spacing, y, self.grid_size, self.grid_size)
            keys.append((letter, rect))
        return keys
    
    


