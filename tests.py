#!/usr/bin/env python

from lambda_calculus import *
from helpers import *

'''
Tests for Boolean Logic
'''

assert TRUE(lambda _: True)(lambda _: False) == True
assert FALSE(lambda _: True)(lambda _: False) == False
assert NOT(TRUE)(lambda _: True)(lambda _: False) == False
assert NOT(FALSE)(lambda _: True)(lambda _: False) == True
assert OR(TRUE)(TRUE)(lambda _: True)(lambda _: False) == True
assert OR(TRUE)(FALSE)(lambda _: True)(lambda _: False) == True
assert OR(FALSE)(TRUE)(lambda _: True)(lambda _: False) == True
assert OR(FALSE)(FALSE)(lambda _: True)(lambda _: False) == False
assert AND(TRUE)(TRUE)(lambda _: True)(lambda _: False) == True
assert AND(TRUE)(FALSE)(lambda _: True)(lambda _: False) == False
assert AND(FALSE)(TRUE)(lambda _: True)(lambda _: False) == False
assert AND(FALSE)(FALSE)(lambda _: True)(lambda _: False) == False
assert IF(TRUE)(lambda _: "Yes")(lambda _: "No") == "Yes"
assert IF(FALSE)(lambda _: "Yes")(lambda _: "No") == "No"

''' 
Tests for Integers and Arithmetic
'''

assert ZERO(lambda x: x+1)(0) == 0
assert ONE(lambda x: x+1)(0) == 1
assert TWO(lambda x: x+1)(0) == 2
assert ADD(ONE)(ONE)(lambda x: x+1)(0) == 2
assert ADD(ONE)(TWO)(lambda x: x+1)(0) == 3
assert ADD(TWO)(ONE)(lambda x: x+1)(0) == 3
assert ADD(TWO)(TWO)(lambda x: x+1)(0) == 4
assert MULT(THREE)(TWO)(lambda x: x+1)(0) == 6
assert MULT(TWO)(THREE)(lambda x: x+1)(0) == 6
assert PRED(THREE)(lambda x: x+1)(0) == 2
assert PRED(FOUR)(lambda x: x+1)(0) == 3
assert MINUS(FOUR)(ONE)(lambda x: x+1)(0) == 3 
assert MINUS(FOUR)(THREE)(lambda x: x+1)(0) == 1

''' 
Tests for Integer comparisons
'''

assert IS_ZERO(ZERO)(lambda _: True)(lambda _: False) == True
assert IS_ZERO(ONE)(lambda _: True)(lambda _: False) == False
assert IS_ZERO(TWO)(lambda _: True)(lambda _: False) == False
assert IF(IS_ZERO(ZERO))(lambda _: "Yes")(lambda _: "No") == "Yes"
assert IF(IS_ZERO(ONE))(lambda _: "Yes")(lambda _: "No") == "No"
assert EQ(ONE)(ONE)(lambda _: True)(lambda _: False) == True
assert EQ(SUCC(SUCC(SUCC(SUCC(ZERO)))))(ADD(TWO)(TWO))(lambda _: True)(lambda _: False) == True
assert LT(FOUR)(THREE)(lambda _: True)(lambda _: False) == True
assert LT(THREE)(FOUR)(lambda _: True)(lambda _: False) == False
assert LT(THREE)(THREE)(lambda _: True)(lambda _: False) == False
assert GT(FOUR)(THREE)(lambda _: True)(lambda _: False) == False
assert GT(THREE)(FOUR)(lambda _: True)(lambda _: False) == True
assert GT(THREE)(THREE)(lambda _: True)(lambda _: False) == False
assert GE(THREE)(THREE)(lambda _: True)(lambda _: False) == True
assert GE(THREE)(TWO)(lambda _: True)(lambda _: False) == False
assert GE(THREE)(FOUR)(lambda _: True)(lambda _: False) == True

'''
Tests for recursive functions
'''

assert FACTORIAL(SUCC(FOUR))(lambda x: x+1)(0) == 120
assert FIBONACCI(FOUR)(lambda x: x+1)(0) == 5
assert DIVIDE(MULT(FOUR)(TWO))(THREE)(lambda x: x+1)(0) == 2
assert REMAINDER(MULT(FOUR)(TWO))(THREE)(lambda x: x+1)(0) == 2
assert REMAINDER(TEN)(FOUR)(lambda x: x+1)(0) == 2

'''
Tests for Lists
'''
l = CONS(ONE)(CONS(TWO)(CONS(THREE)(CONS(FOUR)(NIL))))
k = MAP(MULT(TEN))(l)
assert HEAD(l)(lambda x: x+1)(0) == 1
assert HEAD(TAIL(l))(lambda x: x+1)(0) == 2
assert HEAD(TAIL(TAIL(k)))(lambda x: x+1)(0) == 30
assert HEAD(TAIL(TAIL(TAIL(k))))(lambda x: x+1)(0) == 40
assert LEN(l)(lambda x: x+1)(0) == 4
assert LEN(APPEND(l)(FIVE))(lambda x: x+1)(0) == 5
assert LAST(APPEND(l)(FIVE))(lambda x: x+1)(0) == 5
assert HEAD(REVERSE(l))(lambda x: x+1)(0) == 4


LONG_LIST = CONS(TEN)(CONS(TWO)(CONS(FIVE)(CONS(THREE)(CONS(ONE)(CONS(SIX)(CONS(SEVEN)(CONS(FOUR)(CONS(TWO)(CONS(THREE)(CONS(FOUR)(CONS(EIGHT)(CONS(NINE)(NIL)))))))))))))
assert churchlist_to_list(SORT(LONG_LIST)) == [1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 8, 9, 10]
