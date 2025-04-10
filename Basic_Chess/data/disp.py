import pygame as pg
from data.board import *
import os
import numpy as np
import math
import sys

def load_png(name):
    # First try to find the file using the executable's directory
    try:
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        fullname = os.path.join(base_path, "data", "assets", name)
        
        # If above path doesn't exist, try relative to current working directory
        if not os.path.exists(fullname):
            fullname = os.path.join(os.getcwd(), "data", "assets", name)
            
        # If that still doesn't work, try just the direct path
        if not os.path.exists(fullname):
            fullname = os.path.join("data", "assets", name)
        
        img = pg.image.load(fullname)
        if img.get_alpha() is None:
            img = img.convert()
        else:
            img = img.convert_alpha()
        return img
    except Exception as e:
        print(f"Cannot load image: {name}")
        print(f"Error: {e}")
        print(f"Attempted path: {fullname}")
        print(f"Current working directory: {os.getcwd()}")
        raise SystemExit
        

class disp:
    def __init__(self):
        self.screen = pg.display.set_mode((700, 700))
        self.clock = pg.time.Clock()
        self.running = False

        self.board = load_png('chess_board.png')
        imagerect = self.board.get_rect()
        imagerect.center = self.screen.get_rect().center
        self.coords = imagerect
        self.state = np.zeros((8, 8))
        self.highlighted = False
        self.xcoord = False
        self.ycoord = False

        self.piecedict = {}
        self.piecedict[1] = load_png('wrook.png')
        self.piecedict[2] = load_png('wknight.png')
        self.piecedict[3] = load_png('wbishop.png')
        self.piecedict[4] = load_png('wqueen.png')
        self.piecedict[5] = load_png('wking.png')
        self.piecedict[6] = load_png('bpawn.png')
        self.piecedict[7] = load_png('brook.png')
        self.piecedict[8] = load_png('bknight.png')
        self.piecedict[9] = load_png('bbishop.png')
        self.piecedict[10] = load_png('bqueen.png')
        self.piecedict[11] = load_png('bking.png')
        self.piecedict[12] = load_png('wpawn.png')
        
    def pop(self):
        self.pieceSurface.fill((0, 0, 0, 0))
        for i in range(8):
            for j in range(8):
                if self.state[i, j] != 0:
                    coords = (45+79*i, 45+79*j)
                    self.pieceSurface.blit(self.piecedict[self.state[i, j]], coords)
                    # print(f"{self.state[i, j]} blitted")
                    

    def update(self, boardpos):
        self.state = boardpos

    def highlight(self, x, y, color):
        if x >= 25 and x <= 675 and y >= 25 and y<= 675:
            x = x - 25
            y = y - 25
            self.xcoord = math.floor(x/80)
            self.ycoord = math.floor(y/80)
            hxpos = 30 + self.xcoord*80
            hypos = 32 + self.ycoord*80

            if self.boardarray.state[self.xcoord, self.ycoord] != 0:
                self.selectPieceCoords = (self.xcoord, self.ycoord)
                self.selectedPiece = self.boardarray.state[self.xcoord, self.ycoord]
                self.screen.fill(rect=pg.Rect(hxpos, hypos, 80, 80), color=pg.Color(color[0], color[1], color[2], color[3]))
            else: print('blank square')
            # pg.display.update()
            # self.screen.blit(highlight, (xpos, ypos))



    def launch(self):
        pg.init()
        pg.display.set_caption('Chess')
        self.running = True
        self.pieceSurface = pg.surface.Surface((700,700), pg.SRCALPHA)
        self.boardarray = board()
        self.boardarray.restart()
        self.boardarray.populate()
        print(self.boardarray.state)
        self.update(self.boardarray.state)
        self.boardarray.flip()
        self.update(self.boardarray.state)

        while self.running:
            self.screen.fill((239, 242, 196))
            self.screen.blit(self.board, self.coords)
            self.pop()
            self.screen.blit(self.pieceSurface, (0, 0))

            if self.highlighted == True:
                selCol = [80, 119, 181, 255]
                self.highlight(xMouse, yMouse, selCol)


            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

                if event.type == pg.MOUSEBUTTONUP:
                    mousepos = pg.mouse.get_pos()
                    xMouse = mousepos[0]
                    yMouse = mousepos[1]

                    nowxcoord = math.floor((xMouse-25)/80)
                    nowycoord = math.floor((yMouse-25)/80)

                    if self.highlighted == True:
                        self.highlighted = False
                        

                        # If possible to move
                        if self.boardarray.move(self.selectPieceCoords[0], self.selectPieceCoords[1], nowxcoord, nowycoord):
                            self.boardarray.state[self.xcoord, self.ycoord] = 0
                            self.boardarray.state[nowxcoord, nowycoord] = self.selectedPiece
                            self.boardarray.flip()
                            self.update(self.boardarray.state)
                            print(self.boardarray.state)
                        
                    
                    else:
                        if self.boardarray.state[nowxcoord, nowycoord] != 0:
                            self.highlighted = True
                            # print(mousepos)
                            board.clickHandle(x=xMouse, y=yMouse)
                
                if event.type == pg.KEYUP: 
                    if event.key == pg.K_r:
                        self.boardarray.restart()
                        self.update(self.boardarray.state)
                        print('Board reset')
                    if event.key == pg.K_f:
                        self.boardarray.flip()
                        self.update(self.boardarray.state)
                        print(self.boardarray.state)
                        print('Board flipped')



            
            


            pg.display.flip()
            self.clock.tick(60)
            

        
        pg.quit()


