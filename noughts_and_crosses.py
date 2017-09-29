#!/usr/bin/env python

import sys

from gamelib import *
from lambda_calculus import *
from helpers import *

def cls():
    sys.stderr.write("\x1b[2J\x1b[H")

def display_game(GRID):
    cls()
    print_grid(GRID)

def get_input(PLAYER):
        print "Player ", church_to_int(PLAYER)
        I = int_to_church(int(raw_input("which row: ")))
        J = int_to_church(int(raw_input("which column:" )))
        return(PAIR(I)(J))

def display_winner(WINNER):
    print "Player ", church_to_int(WINNER), "won!"
    return

def main():

    # Initialize
    cls()
    PLAYER = ONE
    GAMEOVER  = FALSE
    WINNER = ZERO
    GRID_SIZE = THREE
    GRID = INIT_LIST(GRID_SIZE)(INIT_LIST(GRID_SIZE)(ZERO))

    # Play
    while(church_to_boolean(NOT(GAMEOVER))):
        
        display_game(GRID)
        MOVE = get_input(PLAYER)
        GRID  = GRID_SET_ELEMENT(MOVE(FST))(MOVE(SND))(PLAYER)(GRID)
        GAMEOVER = OR(IS_WINNER(PLAYER)(GRID))((IS_GRID_FULL)(GRID))
        WINNER = IF(AND(GAMEOVER)(IS_WINNER(PLAYER)(GRID)))(lambda _: ADD(PLAYER)(WINNER))(lambda _: WINNER)
        PLAYER = ADD(REMAINDER(PLAYER)(TWO))(ONE)

    display_winner(WINNER)

main()
