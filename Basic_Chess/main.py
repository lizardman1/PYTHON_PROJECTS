from data.board import *
from data.disp import disp
import pygame as pg
import sys

sys.stdout = open('log.txt', 'w')

# board = board()
# board.restart()
# board.populate()
# print(board.state)

screen = disp()
screen.launch()