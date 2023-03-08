import pygame as pg
import sys
from settings import *
from Board import Board
import numpy as np

class Game():
    def  __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        ## make a array with objects loaded from file later
        self.Board = Board()
        self.turn = 1
        

    
    def new_game(self):
        pass

    def update(self):
        pg.display.flip()
        self.clock.tick(FPS)
        pg.display.set_caption(f"FPS: {self.clock.get_fps() : .1f}")

    def draw(self):
        self.screen.fill('black')
        self.Board.draw(self.screen)
        self.draw_turn()

    def draw_turn(self):
        if self.turn == 1:
           pg.draw.circle(self.screen, RED,(25 , 25), 10)
        elif self.turn == -1:
           pg.draw.circle(self.screen, YELLOW, (25 , 25), 10)


    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                x, y = pg.mouse.get_pos()
                col = self.get_col_from_mouse_pos(x, y)
                move_made = self.Board.move(col,self.turn)
                print(self.Board.checkwin(self.turn))
                if move_made:
                    self.turn *= -1
                
                

    def get_col_from_mouse_pos(self, x, y):
        col = int(np.floor((x + self.Board.margin)/115)) - 1
        return col

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()



