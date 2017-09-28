#!/usr/bin/env python

from lambda_calculus import *


'''
Define some symbols
'''

SPACE = ZERO
NOUGHT = ONE
CROSS = TWO

'''
Initialise the grid
'''

ROW0 = CONS(ZERO)(CONS(ZERO)(CONS(ZERO)(NIL)))
ROW1 = CONS(ZERO)(CONS(ZERO)(CONS(ZERO)(NIL)))
ROW2 = CONS(ZERO)(CONS(ZERO)(CONS(ZERO)(NIL)))
GRID = CONS(ROW0)(CONS(ROW1)(CONS(ROW2)(NIL)))


# GET_ELEMENT = lambda g: lambda x: lambda y: HEAD(y(TAIL)(MAP(HEAD)(x((MAP)(TAIL))(g))))
        
GET_GRID_ELEMENT = lambda j: lambda i: lambda g: HEAD(i(TAIL)(HEAD(j(TAIL)(g))))

GRID_SET_ELEMENT_STUB = lambda f: lambda j: lambda i: lambda v: lambda g: IF(IS_ZERO(j))(lambda _: CONS(SET_ELEMENT(i)(v)(HEAD(g)))(TAIL(g)))(lambda _: CONS(HEAD(g))(f(PRED(j))(i)(v)(TAIL(g))))
GRID_SET_ELEMENT = lambda j: lambda i: lambda v: lambda g: Z(GRID_SET_ELEMENT_STUB)(j)(i)(v)(g)

TRANSPOSE_STUB = lambda f: lambda g: IF(IS_NIL(HEAD(g)))(lambda _: NIL)(lambda _: CONS(MAP(HEAD)(g))(f(MAP(TAIL)(g))))
TRANSPOSE = lambda g: Z(TRANSPOSE_STUB)(g)

GET_ROW = lambda j: lambda g: HEAD(j(TAIL)(g))
GET_COLUMN = lambda j: lambda g: GET_ROW(j)(TRANSPOSE(g))


'''
Count the number of symbols s in a list l
'''

COUNT_SYMBOL = lambda s: lambda l: LEN(FILTER(EQ(s))(l))

''' 
Build new list out of the grids diagonal elements 
'''
DIAGONAL_STUB = lambda f: lambda g: IF(IS_NIL(g))(g)(lambda _: CONS(HEAD(MAP(HEAD)(g))))(lambda _: f(MAP(TAIL)(TAIL(g))))
DIAGONAL = lambda g: Z(DIAGONAL_STUB)(g)

'''
From a grid g generate the winning positions to check
i.e. all the rows, columns and diagonals
'''

WINNING_POSITIONS = lambda g: EXTEND(EXTEND(g)(TRANSPOSE(g)))(CONS(DIAGONAL(g))(CONS(DIAGONAL(MAP(REVERSE)(g)))(NIL)))

# Does symbol "s" on grid "g" have a winning position
# Call after every move

IS_WINNER = lambda s: lambda g: IF(GT(ZERO)(LEN(FILTER(EQ(LEN(g)))(MAP((COUNT_SYMBOL)(s))(WINNING_POSITIONS(g))))))(lambda _: TRUE)(lambda _: FALSE)

# Is the grid full ( i.e. we cannot make any more moves  )

IS_GRID_FULL = lambda g: IF(IS_ZERO(LEN(FILTER(GT(ZERO))(MAP(COUNT_SYMBOL(SPACE))(g)))))(lambda _: TRUE)(lambda _: FALSE)



