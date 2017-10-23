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
Natural Numbers
'''

ZERO = lambda x: lambda y: y
SUCC = lambda n: lambda f: lambda x: f(n(f)(x))

ONE = SUCC(ZERO)
TWO = SUCC(SUCC(ZERO))
THREE = SUCC(SUCC(SUCC(ZERO)))
FOUR = SUCC(THREE)
FIVE = SUCC(FOUR)
SIX = SUCC(FIVE)
SEVEN = SUCC(SIX)
EIGHT = SUCC(SEVEN)
NINE = SUCC(EIGHT)
TEN = SUCC(NINE)

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

MINUS = lambda m: lambda n: m(PRED)(n)

'''
Comparisons
'''

IS_ZERO = lambda n: n(lambda _: FALSE)(TRUE)
EQ = lambda m: lambda n: AND(IS_ZERO(MINUS(m)(n)))(IS_ZERO(MINUS(n)(m)))
GT = lambda m: lambda n: AND(IS_ZERO(MINUS(n)(m)))(NOT(IS_ZERO(MINUS(m)(n)))) 
LT = lambda m: lambda n: AND(NOT(IS_ZERO(MINUS(n)(m))))(IS_ZERO(MINUS(m)(n))) 
GE = lambda m: lambda n: NOT(LT(m)(n))
LE = lambda m : lambda n: OR(EQ(m)(n))(LT(m)(n))


'''
Recursive Functions
Requires the Z combinator
'''
Z = lambda f: (lambda x: f(lambda y: (x)(x)(y)))(lambda x: f(lambda y: (x)(x)(y)))
g = lambda f: lambda n: IF(IS_ZERO(n))(lambda _: ONE)(lambda _: (MULT(n)(f(PRED(n)))))

FACTORIAL = lambda n: Z(g)(n)

fi = lambda f: lambda m: IF(OR(IS_ZERO(m))(IS_ZERO(PRED(m))))(lambda _: ONE)(lambda _: ADD(f(PRED(m)))(f(PRED(PRED(m)))))
FIBONACCI = lambda n: Z(fi)(n)


# Divide
# Variable "c" counts recursion depth as we recursively subtract b from a 
DIV = lambda f: lambda c: lambda a: lambda b: IF(GT)(b)(a)(lambda _: c)(lambda _: f(SUCC(c))(a)(MINUS(a)(b)))
DIVIDE = lambda a: lambda b: Z(DIV)(ZERO)(a)(b)


REM = lambda f: lambda a: lambda b: IF(GT)(b)(a)(lambda _: b)(lambda _: f(a)(MINUS(a)(b)))
REMAINDER = lambda a: lambda b: Z(REM)(a)(b)


# Recursive multiplication
# This is multiplication as repeated addition

m = lambda f: lambda a: lambda b: IF(IS_ZERO)(b)(lambda _: ZERO)(lambda _: ADD(a)(f(a)(PRED(b))))
RMULT = lambda a: lambda b: Z(m)(a)(b)


# Euclids gcd algorithm
GCD_STUB = lambda f: lambda a: lambda b: IF(IS_ZERO(b))(lambda _: a)(lambda _: f(b)(REMAINDER(a)(b)))
GCD = lambda a: lambda b: Z(GCD_STUB)(a)(b)

'''
Lists
Generated as pairs of pairs
NIL is the empty list
IS_NIL tests for the empty list
'''

NIL = PAIR(TRUE)(TRUE)
IS_NIL = lambda l: l(FST)
CONS = lambda h: lambda t: PAIR(FALSE)(PAIR(h)(t))

HEAD = lambda l: IF(NOT(IS_NIL(l)))(lambda _: l(SND)(FST))(lambda _: NIL)
TAIL = lambda l: IF(NOT(IS_NIL(l)))(lambda _: l(SND)(SND))(lambda _: NIL)

MAP_STUB = lambda f: lambda g: lambda l: IF(IS_NIL(l))(lambda _: l)(lambda _: CONS((g)(HEAD(l)))(f(g)(TAIL(l))))
MAP = lambda g: lambda l: Z(MAP_STUB)(g)(l)

# APPEND appends a single element to an existing list 
APPEND_STUB = lambda f: lambda l: lambda e: IF(IS_NIL(l))(lambda _: CONS(e)(l))(lambda _: CONS(HEAD(l))(f(TAIL(l))(e)))
APPEND = lambda l: lambda e: Z(APPEND_STUB)(l)(e)

LEN_STUB = lambda f: lambda c: lambda l: IF(IS_NIL(l))(lambda _: c)(lambda _: f(SUCC(c))(TAIL(l)))
LEN = lambda l: Z(LEN_STUB)(ZERO)(l)

LAST_STUB = lambda f: lambda l: IF(IS_NIL(TAIL(l)))(lambda _: HEAD(l))(lambda _: f(TAIL(l)))
LAST  = lambda l: Z(LAST_STUB)(l)

REVERSE_STUB = lambda f: lambda l: IF(IS_NIL(l))(lambda _: l)(lambda _: APPEND(f(TAIL(l)))(HEAD(l)))
REVERSE = lambda l: Z(REVERSE_STUB)(l)

FOLDR_STUB = lambda f: lambda g: lambda c: lambda l: IF(IS_NIL(l))(lambda _: c)(lambda _: g(HEAD(l))(f(g)(c)(TAIL(l))))
FOLDR = lambda g: lambda c: lambda l: Z(FOLDR_STUB)(g)(c)(l)

# EXTEND joins two lists
EXTEND = lambda a: lambda b: FOLDR(CONS)(b)(a)

FILTER_STUB = lambda f: lambda p: lambda l: IF(IS_NIL(l))(lambda _: l)(lambda _: IF(p(HEAD(l)))(lambda _: CONS(HEAD(l))(f(p)(TAIL(l))))(lambda _: f(p)(TAIL(l))))
FILTER = lambda p: lambda l: Z(FILTER_STUB)(p)(l)

# GET an element of a list
GET_ELEMENT_STUB = lambda f: lambda i: lambda l: IF(IS_ZERO(i))(lambda _: HEAD(l))(lambda _: f(PRED(i))(TAIL(l)))
GET_ELEMENT = lambda i: lambda l: Z(GET_ELEMENT_STUB)(i)(l) 

# SET an element of a list
SET_ELEMENT_STUB = lambda f:  lambda i: lambda v: lambda l: IF(IS_ZERO(i))(lambda _: CONS(v)(TAIL(l)))(lambda _: CONS(HEAD(l))(f(PRED(i))(v)(TAIL(l))))
SET_ELEMENT = lambda i: lambda v: lambda l: Z(SET_ELEMENT_STUB)(i)(v)(l)

# Quick Sort

SORT_STUB = lambda f: lambda l: IF(IS_NIL(l))(lambda _: l)(lambda _: EXTEND(APPEND(f(FILTER(LE(HEAD(l)))(TAIL(l))))(HEAD(l)))(f(FILTER(GT(HEAD(l)))(TAIL(l)))))
SORT = lambda l: Z(SORT_STUB)(l)

RANGE_STUB = lambda f: lambda s: lambda e: IF(EQ(s)(e))(lambda _: NIL)(lambda _: CONS(s)(f(SUCC(s))(e)))
RANGE = lambda s: lambda e: Z(RANGE_STUB)(s)(e)

SIEVE_STUB = lambda f: lambda l: IF(IS_NIL(l))(lambda _: l)(lambda _: CONS(HEAD(l))(f(FILTER(lambda X: NOT(IS_ZERO(REMAINDER(HEAD(l))(X))))(l))))
SIEVE = lambda l: Z(SIEVE_STUB)(l)



