import pygame as pg
import sys
from settings import *
from Board import Board

class Game():
    def  __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        ## make a array with objects loaded from file later
        self.Board = Board()

    
    def new_game(self):
        pass

    def update(self):
        pg.display.flip()
        self.clock.tick(FPS)
        pg.display.set_caption(f"FPS: {self.clock.get_fps() : .1f}")

    def draw(self):
        self.screen.fill('black')
        self.Board.draw(self.screen)

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                row, col = self.Board.move(1,1)
                print(self.Board.checkwin(1))
                


    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()



