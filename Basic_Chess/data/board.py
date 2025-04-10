import numpy as np
from data.pieces.bishop import bishop
from data.pieces.king import king
from data.pieces.queen import queen
from data.pieces.pawn import pawn
from data.pieces.rook import rook
from data.pieces.knight import knight
import pygame as pg
import math

class board:
    # populate updates the positions on the state attribute
    def __init__(self):
        self.state = np.zeros((8, 8))
        self.flipped = False
        self.turn = 'white'

    def populate(self):

        self.state = np.zeros((8, 8))
        print(self.state[self.pieces['bishop1'].pos1, self.pieces['bishop1'].pos2])
        for piece in self.pieces.values():
            self.state[int(piece.pos1), int(piece.pos2)] = piece.key

    def clickHandle(x, y):
        pass

    def convChessCoord(self, pos1, pos2):
        lettersx = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H'}
        lettersy = {0: '8', 1: '7', 2: '6', 3: '5', 4: '4', 5: '3', 6: '2', 7: '1'}
        return lettersx[pos1] + lettersy[pos2]

    def flip(self):
        self.state = np.flip(self.state, 1)
        
        if self.flipped == True:
            self.flipped = False
        else: self.flipped = True

        for x in self.pieces:
            self.pieces[x].pos2 = 7 - self.pieces[x].pos2
            print(self.pieces[x].pos1, self.pieces[x].pos2)

    def checkCheck(self, turn):
        pass

    def move(self, xbefore, ybefore, xafter, yafter):
        pieceTake = 'not selected'
        piece = False
        for pieceSel in self.pieces:
            
            if xbefore == self.pieces[pieceSel].pos1 and ybefore == self.pieces[pieceSel].pos2:
                piece = pieceSel
                # Piece is the selected pieces object name
                # print(self.pieces[piece].canMove())
            
            if xafter == self.pieces[pieceSel].pos1 and yafter == self.pieces[pieceSel].pos2:
                pieceTake = pieceSel
                # PieceTake is the piece that the selected piece is taking if it exists

                
            
        # Checks if the move is on the board and in a direction for the type of chess piece and if it is your turn
        if piece != False:
            if type(self.pieces[piece]) is pawn:

                # If there is a piece on either diagonal, say you can take it
                left = False
                right = False

                if pieceTake != 'not selected':
                    if self.pieces[pieceTake].pos1 == self.pieces[piece].pos1 - 1 and self.pieces[pieceTake].pos2 == self.pieces[piece].pos2 - 1 and self.pieces[pieceTake].colour != self.pieces[piece].colour:
                        left = True
                        print('left is true')
                    if self.pieces[pieceTake].pos1 == self.pieces[piece].pos1 + 1 and self.pieces[pieceTake].pos2 == self.pieces[piece].pos2 - 1 and self.pieces[pieceTake].colour != self.pieces[piece].colour:
                        right = True
                        print('right is true')

                if self.pieces[piece].check(xafter, yafter, xbefore, ybefore, self.state, self.flipped, left, right) and self.pieces[piece].colour == self.turn and (pieceTake == 'not selected' or self.pieces[pieceTake].colour != self.pieces[piece].colour):
                    self.pieces[piece].pos1 = xafter
                    self.pieces[piece].pos2 = yafter
                    self.pieces[piece].moved = True

                    if pieceTake != 'not selected':
                        print(f'{self.pieces[piece]} took {self.pieces[pieceTake]} on {self.convChessCoord(xafter, yafter)}')
                        del self.pieces[pieceTake]
                    else: print(f'{self.pieces[piece]} moved to {self.convChessCoord(xafter, yafter)}')
                        
                    
                    if self.turn == 'white':
                        self.turn = 'black'
                    else: self.turn = 'white'
                    
                    return True

            elif self.pieces[piece].check(xafter, yafter, xbefore, ybefore, self.state, self.flipped) and self.pieces[piece].colour == self.turn and (pieceTake == 'not selected' or self.pieces[pieceTake].colour != self.pieces[piece].colour):
                self.pieces[piece].pos1 = xafter
                self.pieces[piece].pos2 = yafter
                
                if pieceTake != 'not selected':
                    print(f'{self.pieces[piece]} took {self.pieces[pieceTake]} on {self.convChessCoord(xafter, yafter)}')
                    del self.pieces[pieceTake]
                else: print(f'{self.pieces[piece]} moved to {self.convChessCoord(xafter, yafter)}')
                
                if self.turn == 'white':
                    self.turn = 'black'
                else: self.turn = 'white'
                
                return True
            else: return False



    def restart(self):
        self.pieces = {}
        
        self.pieces['bishop1'] = bishop(pos1=2, pos2=0, colour='white', name='b1')
        self.pieces['bishop2'] = bishop(pos1=5, pos2=0, colour='white', name='b2')
        self.pieces['bishop3'] = bishop(pos1=2, pos2=7, colour='black', name='b3')
        self.pieces['bishop4'] = bishop(pos1=5, pos2=7, colour='black', name='b4')
        self.pieces['knight1'] = knight(pos1=1, pos2=0, colour='white', name='k1')
        self.pieces['knight2'] = knight(pos1=6, pos2=0, colour='white', name='k2')
        self.pieces['knight3'] = knight(pos1=1, pos2=7, colour='black', name='k3')
        self.pieces['knight4'] = knight(pos1=6, pos2=7, colour='black', name='k4')
        self.pieces['rook1'] = rook(pos1=0, pos2=0, colour='white', name='r1')
        self.pieces['rook2'] = rook(pos1=7, pos2=0, colour='white', name='r2')
        self.pieces['rook3'] = rook(pos1=0, pos2=7, colour='black', name='r3')
        self.pieces['rook4'] = rook(pos1=7, pos2=7, colour='black', name='r4')
        self.pieces['queen1'] = queen(pos1=3, pos2=0, colour='white', name='q1')
        self.pieces['queen2'] = queen(pos1=3, pos2=7, colour='black', name='q2')
        self.pieces['king1'] = king(pos1=4, pos2=0, colour='white', name='ki1')
        self.pieces['king2'] = king(pos1=4, pos2=7, colour='black', name='ki2')
        self.pieces['pawn1'] = pawn(pos1=0, pos2=1, colour='white', name='p1')
        self.pieces['pawn2'] = pawn(pos1=1, pos2=1, colour='white', name='p2')
        self.pieces['pawn3'] = pawn(pos1=2, pos2=1, colour='white', name='p3')
        self.pieces['pawn4'] = pawn(pos1=3, pos2=1, colour='white', name='p4')
        self.pieces['pawn5'] = pawn(pos1=4, pos2=1, colour='white', name='p5')
        self.pieces['pawn6'] = pawn(pos1=5, pos2=1, colour='white', name='p6')
        self.pieces['pawn7'] = pawn(pos1=6, pos2=1, colour='white', name='p7')
        self.pieces['pawn8'] = pawn(pos1=7, pos2=1, colour='white', name='p8')
        self.pieces['pawn9'] = pawn(pos1=0, pos2=6, colour='black', name='p9')
        self.pieces['pawn10'] = pawn(pos1=1, pos2=6, colour='black', name='p10')
        self.pieces['pawn11'] = pawn(pos1=2, pos2=6, colour='black', name='p11')
        self.pieces['pawn12'] = pawn(pos1=3, pos2=6, colour='black', name='p12')
        self.pieces['pawn13'] = pawn(pos1=4, pos2=6, colour='black', name='p13')
        self.pieces['pawn14'] = pawn(pos1=5, pos2=6, colour='black', name='p14')
        self.pieces['pawn15'] = pawn(pos1=6, pos2=6, colour='black', name='p15')
        self.pieces['pawn16'] = pawn(pos1=7, pos2=6, colour='black', name='p16')

        self.populate()
        