#!/usr/bin/env python

from numerals import *
from boole import *
from numeric_tests import *


''' 
The Z combinator

Z = lambda f: (lambda x.f(lambda y: x(x)(y)))(lambda x: f(lambda y: x(x)(y)))
is required to make the recursive lambda in python ? 

'''
Z = lambda f: (lambda x: f(lambda y: (x)(x)(y)))(lambda x: f(lambda y: (x)(x)(y)))

g = lambda f: lambda n: ((one) if church_to_boolean(is_zero(n)) else (mult(n)(f((pred)(n)))))

# Attempt to expand python ( t if c else a ) into lambda if_then_else ) but fails...
# h = lambda f: lambda n: (lambda c: lambda t: lambda a: (is_zero(n))(one)(mult(n)(f((pred)(n)))))

h = lambda f: lambda n: if_then_else(is_zero(n))(one)(mult(n)(f((pred)(n))))

fact = lambda n: Z(g)(n)
fact2 = lambda n: Z(h)(n)

assert church_to_int(fact(zero)) == 1

assert church_to_int(fact(four)) == 24
#assert church_to_int(fact2(four)) == 24
