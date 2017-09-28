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
    while(church_to_boolean(NOT(IS_WINNER(PLAYER)(GRID)))):

        # CLEAR AND DISPLAY GRID ( i.e. Take church grid and render it )
        cls()
        #print_grid(WINNING_POSITIONS(GRID))
        #print church_to_boolean(NOT(IS_WINNER(PLAYER)(GRID)))
        print_grid(GRID)
        # GET player 1 INPUT
        I = int_to_church(int(raw_input("which row: ")))
        J = int_to_church(int(raw_input("which column:" )))
        GRID  = GRID_SET_ELEMENT(I)(J)(PLAYER)(GRID)

        cls()
        print_grid(GRID)

        PLAYER = ADD(REMAINDER(PLAYER)(TWO))(ONE)

        # CONVERT TO CHURCH (i.e. generate new church grid)
        # Any body won ( if so break and announce winner)
        # any more moves ( otherwise break and announce draw )
        # get player 2 input (or generate computer move)
        # Anybody won ( if so break and announce winner )
        # any more moves ( otherwise breake and announce draw )
    # Print Winner

main()
