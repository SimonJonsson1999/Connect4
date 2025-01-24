import pygame as pg
import math as math
import numpy as np
from scipy import signal
from settings import *
class Board():
    def __init__(self):
        self.nrows = 6
        self.ncols = 7
        self.state = np.zeros([self.nrows,self.ncols])
        self.margin = 50
        self.smargin = 5

    def draw(self, screen):
        backboard = pg.Rect(self.margin, self.margin, WIDTH - 2*self.margin, HEIGTH - 2*self.margin)
        pg.draw.rect(screen, BLUE, backboard)
        for i in range(self.nrows):
             for j in range(self.ncols):
                if self.state[i,j] == 0:
                    pg.draw.circle(screen, WHITE, ( (j+1)*115 , (i+1)* 75), 25)

                elif self.state[i,j] == 1:
                    pg.draw.circle(screen, RED, ( (j+1)*115 , (i+1)* 75), 25)

                elif self.state[i,j] == -1:
                    pg.draw.circle(screen, YELLOW, ( (j+1)*115 , (i+1)* 75), 25)

        
    
                
    def move(self, col, player):
        if col is None or not (0 <= col < self.ncols):
            print("Invalid column:", col)
            return False

        empty_rows = np.argwhere(self.state[:, col] == 0).flatten()
        if empty_rows.size > 0:
            lowest_empty_row = empty_rows[-1] 
            self.state[lowest_empty_row, col] = player
            return True
        else:
            return False
        
    def checkwin(self, player):
        horizontal_kernel = np.array([[ 1, 1, 1, 1]])
        vertical_kernel = np.transpose(horizontal_kernel)
        diag1_kernel = np.eye(4, dtype=np.uint8)
        diag2_kernel = np.fliplr(diag1_kernel)
        detection_kernels = [horizontal_kernel, vertical_kernel, diag1_kernel, diag2_kernel]
        for kernel in detection_kernels:
            if (signal.convolve2d(self.state == player, kernel, mode = 'valid') >= 4).any():
                return True
            
        return False
    

    def is_full(self):
        return np.all(self.state != 0)

    def is_valid_location(self, col):
        return self.state[0, col] == 0

    def copy(self):
        new_board = Board()
        new_board.state = np.copy(self.state)
        return new_board
    

    


