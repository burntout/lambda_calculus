#!/usr/bin/env python
from boole import *
from numerals import *

'''
test for equality 
'''

ret_false = lambda x: false
is_zero = lambda n: n(ret_false)(true)


equal = lambda m: lambda n: c_and(is_zero(sub(m)(n)))(is_zero(sub(n)(m)))
gt = lambda m: lambda n: c_not(is_zero(sub(m)(n)))
lt = lambda m: lambda n: c_and(c_not(gt(m)(n)))(c_not(equal(m)(n)))


assert church_to_boolean(is_zero(zero)) == True
assert church_to_boolean(is_zero(one)) == False

assert church_to_boolean(equal(one)(one)) == True
assert church_to_boolean(equal(one)(two)) == False
assert church_to_boolean(equal(two)(one)) == False

assert church_to_boolean(gt(three)(two)) == True
assert church_to_boolean(gt(three)(four)) == False
assert church_to_boolean(gt(three)(three)) == False


assert church_to_boolean(lt(three)(four)) == True
assert church_to_boolean(lt(four)(three)) == False
assert church_to_boolean(lt(four)(four)) == False
