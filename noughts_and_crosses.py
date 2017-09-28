#!/usr/bin/env python

import sys

from gamelib import *
from lambda_calculus import *
from helpers import *


def cls():
    sys.stderr.write("\x1b[2J\x1b[H")


def main():
    # INTIALISE
    cls()
    PLAYER = ONE
    ROW0 = CONS(ZERO)(CONS(ZERO)(CONS(ZERO)(NIL)))
    ROW1 = CONS(ZERO)(CONS(ZERO)(CONS(ZERO)(NIL)))
    ROW2 = CONS(ZERO)(CONS(ZERO)(CONS(ZERO)(NIL)))
    GRID = CONS(ROW0)(CONS(ROW1)(CONS(ROW2)(NIL)))



    # START GAME LOOP
    GAMEOVER  = FALSE
    WINNER = ZERO
    # while(church_to_boolean(NOT(IS_WINNER(PLAYER)(GRID)))):
    while(church_to_boolean(NOT(GAMEOVER))):

        # CLEAR AND DISPLAY GRID ( i.e. Take church grid and render it )
        cls()
        print_grid(GRID)

        # GET player INPUT
        print "Player ", church_to_int(PLAYER)
        I = int_to_church(int(raw_input("which row: ")))
        J = int_to_church(int(raw_input("which column:" )))
        GRID  = GRID_SET_ELEMENT(I)(J)(PLAYER)(GRID)

        cls()
        print_grid(GRID)

        GAMEOVER = OR(IS_WINNER(PLAYER)(GRID))((IS_GRID_FULL)(GRID))

        WINNER = IF(AND(GAMEOVER)(IS_WINNER(PLAYER)(GRID)))(lambda _: ADD(PLAYER)(WINNER))(lambda _: WINNER)
        
        PLAYER = ADD(REMAINDER(PLAYER)(TWO))(ONE)

    print "Player ", church_to_int(WINNER), "won!"

main()
