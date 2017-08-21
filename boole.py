#!/usr/bin/env python

false = lambda x: lambda y: y
true = lambda x: lambda y: x


c_not =  lambda x: x(false)(true)
c_or = lambda x: lambda y: x(true)(y(true)(false))
c_and = lambda x: lambda y: x(y(true)(false))(false)

''' 
define a helper functions 
'''
def church_to_boolean(cb):
    return cb(True)(False)
''' 
define a helper function 
'''

'''
Tests
'''
assert church_to_boolean(false) == False
assert church_to_boolean(true) == True

assert  church_to_boolean(c_not(true)) == False
assert  church_to_boolean(c_not(false)) == True

assert  church_to_boolean(c_and(false)(false)) == False
assert  church_to_boolean(c_and(false)(true)) == False
assert  church_to_boolean(c_and(true)(false)) == False
assert  church_to_boolean(c_and(true)(true)) == True

assert  church_to_boolean(c_or(true)(true)) == True
assert  church_to_boolean(c_or(true)(false)) == True
assert  church_to_boolean(c_or(false)(true)) == True
assert  church_to_boolean(c_or(false)(false)) == False
