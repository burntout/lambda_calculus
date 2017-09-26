#!/usr/bin/env python

'''
define some important constants
snd gives the second element of a pair
fst gives the first element of a pair
'''
zero = lambda x: lambda y: y
snd = lambda x: lambda y: y
fst = lambda x: lambda y: x


''' 
define the successor function
and a generate a few integers
'''
succ =  lambda n: lambda f: lambda x: f(n(f)(x))

one = succ(zero)
two = succ(one)
three = succ(two)
four = succ(three)


'''
define helper functions to convert church numerals to integers
and vice versa
'''

def church_to_int(church):
    return church(lambda x: x+1)(0)

def int_to_church(n):
    return succ(int_to_church(n-1)) if n > 0 else zero

''' 
Define addition, multiplication and exponentiation
add(x)(y) -> x+y
mult(x)(y) -> x*y
expn(x)(y) -> x**y
'''

add = lambda m: lambda n: lambda f: lambda x: m(f)(n(f)(x))
mult = lambda m: lambda n: lambda f: lambda x: m(n(f))(x)
expn = lambda m: lambda n: lambda f: lambda x: n(m)(f)(x)

''' 
Define Kleene's predeccessor function
pair takes a selector 's' and uses it to return the first or second element of a pair 
pzero is a pair of zeros
psucc takes pair p = (a,b) to (b,succ(b))
pred of n returns (n-1)
'''

pair = lambda a: lambda b: lambda s: s(a)(b)
pzero = pair(zero)(zero)
psucc = lambda p: pair(p(snd))(succ(p(snd)))
pred = lambda n: n(psucc)(pzero)(fst)


'''
Create a subtraction function from the predecessor function
sub(m)(n) == m - n
'''

sub = lambda m: lambda n: n(pred)(m)


''' 
Tests
'''

assert church_to_int(one) == 1
assert church_to_int(two) == 2
assert church_to_int(three) == 3 
assert church_to_int(four) == 4 

assert church_to_int(add(one)(one)) == 2
assert church_to_int(mult(four)(three)) == 12
assert church_to_int(expn(two)(three)) == 8

assert church_to_int(pred(four)) == 3
assert church_to_int(sub(four)(three)) == 1
