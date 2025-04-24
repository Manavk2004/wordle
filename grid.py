import pygame
from word import RandomWord
from colors import *
from keyboard_handler import *

pygame.font.init()
FONT = pygame.font.SysFont("arial", 48)


#List for the actual wordle word being stored from words.txt file


class Grid:
    def __init__(self):
        self.num_cols = 5
        self.num_rows = 6
        self.grid_size = 65
        self.grid = [[0 for i in range(self.num_cols)] for j in range(self.num_rows)]
        self.typed_letters = [["" for i in range(self.num_cols)] for j in range(self.num_rows)]
        self.current_col = 0
        self.current_row = 0
        self.actual_wordle = []
        self.word = []
        self.used_keys = {}

        
    

    
    '''
    Draws the actual grid on the screen as well as displaying the letter in each individual box in the grid
    text_rect holds the object of the rectange. It will be displayed as <rect(x, y, w, h)> Pygame takes care of the width and height and will display it perfectly in the center
    '''

    def draw_grid_squares(self, surface):
        squares = []
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                rect = pygame.Rect(column*self.grid_size+450, row*self.grid_size+120, self.grid_size-5, self.grid_size-5)
                squares.append(rect)


                status = self.grid[row][column]

                if status == 2:
                    color = GREEN
                elif status == 1:
                    color = YELLOW
                else:
                    color = BLACK

                pygame.draw.rect(surface, GRAY, rect)
                inset_rect = rect.inflate(-4, -4)
                pygame.draw.rect(surface, color, inset_rect)
    


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

    def replace_l_event(self, event, surface):
        if event.type == pygame.KEYDOWN:
            letter = event.unicode.upper()
            if letter.isalpha() and len(letter) == 1:
                if self.current_col < 5:
                    self.typed_letters[self.current_row][self.current_col] = letter
                    self.word.append(letter)
                    self.current_col += 1

            if self.current_col == 5 and event.key == pygame.K_RETURN:
                if len(self.word) == 5:
                    for letter in self.typed_letters[self.current_row]:
                        self.used_keys[letter] = True
                    self.check()
                    self.draw_grid_squares(surface)
                    self.current_row += 1
                    self.current_col = 0
                    self.word = []
                    
            if event.key == pygame.K_BACKSPACE:
                if self.current_col > 0:
                    self.current_col -= 1
                    self.typed_letters[self.current_row][self.current_col] = ""
                    self.word.pop()


    #Comparing words and indexes

    def got_word(self):
        with RandomWord() as word1:
            self.actual_wordle = list(word1.strip().upper())



    #This method changes the numbers in the main grid so we can assign the numbers to colors which will be displayed on the board
    def check(self):
        if len(self.word) != 5 or len(self.actual_wordle) != 5:
            print("ERROR: invalid lengths")
            print("self.word =", self.word, "len =", len(self.word))
            print("self.actual_wordle =", self.actual_wordle, "len =", len(self.actual_wordle))
            return
        
        used = [False] * 5

        for i in range(5):
            if self.word[i] == self.actual_wordle[i]:
                self.grid[self.current_row][i] = 2
                used[i] = True
        
        for i in range(5):
            if self.word[i] != self.actual_wordle[i]:
                for j in range(5):
                    if self.word[i] == self.actual_wordle[j] and used[j] == False:
                        self.grid[self.current_row][i] = 1
                        used[j] = True
                        break

                



