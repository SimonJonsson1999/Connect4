import pygame as pg
import sys
from settings import *
from Board import Board
from AI import AI
import numpy as np

class Game():
    def  __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        ## make a array with objects loaded from file later
        self.board = Board()
        self.turn = 1
        self.game_over = False
        self.winner = 0  
        self.ai_player = AI(-1, 4)
    
    def update(self):
        pg.display.flip()
        self.clock.tick(FPS)
        pg.display.set_caption(f"FPS: {self.clock.get_fps() : .1f}")

    def draw(self):
        self.screen.fill('black')
        self.board.draw(self.screen)
        self.draw_turn()
        if self.game_over:
            self.display_winner()

    def draw_turn(self):
        if self.turn == 1:
           pg.draw.circle(self.screen, RED,(25 , 25), 10)
        elif self.turn == -1:
           pg.draw.circle(self.screen, YELLOW, (25 , 25), 10)

    def display_winner(self):
        font = pg.font.Font(None, 36)
        if self.winner == 1:
            text = font.render('Red wins!', True, RED)
        elif self.winner == -1:
            text = font.render('Yellow wins!', True, YELLOW)
        else:
            text = font.render('Draw!', True, WHITE)
        text_rect = text.get_rect(center=(RES[0]//2, RES[1]//2))
        self.screen.blit(text, text_rect)


    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            if not self.game_over and event.type == pg.MOUSEBUTTONDOWN and self.turn != self.ai_player.turn:
                x, y = pg.mouse.get_pos()
                col = self.get_col_from_mouse_pos(x, y)
                move_made = self.board.move(col, self.turn)
                if self.board.checkwin(self.turn):
                        self.winner = self.turn
                        self.game_over = True
                if move_made:
                    self.turn *= -1

    def update_game_logic(self):
        if not self.game_over:
            if self.turn == self.ai_player.turn:
                col = self.ai_player.choose_move(self.board, self.turn)
                if col is None:
                    print("No valid move returned by AI")
                    if self.board.is_full():
                        self.winner = 0 
                        self.game_over = True
                        print("Game is a draw")
                    else:
                        print("AI failed to find a valid move, but board is not full.")
                       
                else:
                    if self.board.move(col, self.turn):
                        if self.board.checkwin(self.turn):
                            self.winner = self.turn
                            self.game_over = True
                        else:
                            self.turn *= -1
                
                

    def get_col_from_mouse_pos(self, x, y):
        col = int(np.floor((x + self.board.margin)/115)) - 1
        # print(col)
        return col

    def run(self):
        while True:
            self.check_events()
            self.update_game_logic()
            self.update()
            self.draw()

