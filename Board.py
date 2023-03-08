import pygame as pg
import math as math
import numpy as np
from scipy import signal
from settings import *
class Board():
    # SIZE = 6x7
    def __init__(self):
        self.nrows = 6
        self.ncols = 7
        self.board_state = np.zeros([self.nrows,self.ncols])
        self.margin = 50
        self.smargin = 5
    def draw(self, screen):
        ##TODO ##
        # Improve drawing to be dynamic with respect to window size and margins, will be a headache.
        #  Works fine for implementing and testing logic
        backboard = pg.Rect(self.margin, self.margin, WIDTH - 2*self.margin, HEIGTH - 2*self.margin)
        pg.draw.rect(screen, BLUE, backboard)
        for i in range(self.nrows):
             for j in range(self.ncols):
                if self.board_state[i,j] == 0:
                    pg.draw.circle(screen, WHITE, ( (j+1)*115 , (i+1)* 75), 25)

                elif self.board_state[i,j] == 1:
                    pg.draw.circle(screen, RED, ( (j+1)*115 , (i+1)* 75), 25)

                elif self.board_state[i,j] == -1:
                    pg.draw.circle(screen, YELLOW, ( (j+1)*115 , (i+1)* 75), 25)

        
    
                
    def move(self, col, number):
        index = np.argwhere(self.board_state[:,col] == 0)
        if len(index) > 0:
            if np.max(index) >= 0:
                self.board_state[np.max(index), col] = number
                return True
            return False
        
    
    
    def checkwin(self, player):
        horizontal_kernel = np.array([[ 1, 1, 1, 1]])
        vertical_kernel = np.transpose(horizontal_kernel)
        diag1_kernel = np.eye(4, dtype=np.uint8)
        diag2_kernel = np.fliplr(diag1_kernel)
        detection_kernels = [horizontal_kernel, vertical_kernel, diag1_kernel, diag2_kernel]
        for kernel in detection_kernels:
            if (signal.convolve2d(self.board_state == player, kernel, mode = 'valid') >= 4).any():
                return True
            
        return False

