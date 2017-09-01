#!/usr/bin/env python

'''
Another go  with Lambda calculus
This time though with changes to Booleans, wrapping them in additional lambda
to make them lazy evaluated. 
'''

'''
Booleans
'''

TRUE = lambda x: lambda y: x(lambda z: z)
FALSE = lambda x: lambda y: y(lambda z: z)

NOT = lambda x: x(lambda _: FALSE)(lambda _: TRUE)
OR = lambda x: lambda y: x(lambda _: TRUE)(lambda _: y(lambda _: TRUE)(lambda _: FALSE))
AND = lambda x: lambda y: x(lambda _: y(lambda _: TRUE)(lambda _: FALSE))(lambda _: FALSE)

IF = lambda c: lambda t: lambda e: c(t)(e)

'''
Boolean Tests
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
Natural Numbers
'''

ZERO = lambda x: lambda y: y
SUCC = lambda n: lambda f: lambda x: f(n(f)(x))

ONE = SUCC(ZERO)
TWO = SUCC(SUCC(ZERO))
THREE = SUCC(SUCC(SUCC(ZERO)))
FOUR = SUCC(THREE)

''' 
Math on Natural Numbers
'''


ADD = lambda m: lambda n: lambda f: lambda x: m(f)(n(f)(x))
MULT = lambda m: lambda n: lambda f: lambda x: m(n(f))(x)

'''
Minus via Kleene's Predecessor Function
'''

PAIR = lambda a: lambda b: lambda s: s(a)(b)
FST = lambda x: lambda y: x
SND = lambda x: lambda y: y

ZZ = PAIR(ZERO)(ZERO)
PSUCC = lambda p: PAIR(p(SND))(SUCC(p(SND)))
PRED = lambda n: n(PSUCC)(ZZ)(FST)

MINUS = lambda m: lambda n: n(PRED)(m)

'''
Integer Tests
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
Comparisons
'''

IS_ZERO = lambda n: n(lambda _: FALSE)(TRUE)
EQ = lambda m: lambda n: AND(IS_ZERO(MINUS(m)(n)))(IS_ZERO(MINUS(n)(m)))
LT = lambda m: lambda n: AND(IS_ZERO(MINUS(m)(n)))(NOT(IS_ZERO(MINUS(n)(m)))) 
GT = lambda m: lambda n: AND(NOT(IS_ZERO(MINUS(m)(n))))(IS_ZERO(MINUS(n)(m))) 


'''
Comparison Tests
'''

assert IS_ZERO(ZERO)(lambda _: True)(lambda _: False) == True
assert IS_ZERO(ONE)(lambda _: True)(lambda _: False) == False
assert IS_ZERO(TWO)(lambda _: True)(lambda _: False) == False
assert IF(IS_ZERO(ZERO))(lambda _: "Yes")(lambda _: "No") == "Yes"
assert IF(IS_ZERO(ONE))(lambda _: "Yes")(lambda _: "No") == "No"

assert EQ(ONE)(ONE)(lambda _: True)(lambda _: False) == True
assert EQ(SUCC(SUCC(SUCC(SUCC(ZERO)))))(ADD(TWO)(TWO))(lambda _: True)(lambda _: False) == True

assert LT(FOUR)(THREE)(lambda _: True)(lambda _: False) == False
assert LT(THREE)(FOUR)(lambda _: True)(lambda _: False) == True
assert LT(THREE)(THREE)(lambda _: True)(lambda _: False) == False

assert GT(FOUR)(THREE)(lambda _: True)(lambda _: False) == True
assert GT(THREE)(FOUR)(lambda _: True)(lambda _: False) == False
assert GT(THREE)(THREE)(lambda _: True)(lambda _: False) == False

'''
Recursive Functions
Requires the Z combinator
'''

Z = lambda f: (lambda x: f(lambda y: (x)(x)(y)))(lambda x: f(lambda y: (x)(x)(y)))
g = lambda f: lambda n: IF(IS_ZERO(n))(lambda _: ONE)(lambda _: (MULT(n)(f(PRED(n)))))

FACTORIAL = lambda n: Z(g)(n)


fi = lambda f: lambda m: IF(OR(IS_ZERO(m))(IS_ZERO(PRED(m))))(lambda _: ONE)(lambda _: ADD(f(PRED(m)))(f(PRED(PRED(m)))))
FIBONACCI = lambda n: Z(fi)(n)

assert FACTORIAL(SUCC(FOUR))(lambda x: x+1)(0) == 120
assert FIBONACCI(FOUR)(lambda x: x+1)(0) == 5
