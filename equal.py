#!/usr/bin/env python
from boole import *
from church import *

'''
test for equality 
'''

ret_false = lambda x: false
is_zero = lambda n: n(ret_false)(true)


equal = lambda m: lambda n: c_and(is_zero(sub(m)(n)))(is_zero(sub(n)(m)))


''' 
define a helper functions 
'''
def church_to_boolean(cb):
    return cb(True)(False)

assert church_to_boolean(false) == False
assert church_to_boolean(true) == True

assert church_to_boolean(is_zero(zero)) == True
assert church_to_boolean(is_zero(one)) == False

assert church_to_boolean(equal(one)(one)) == True
assert church_to_boolean(equal(one)(two)) == False
assert church_to_boolean(equal(two)(one)) == False

