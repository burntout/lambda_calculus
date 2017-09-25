#!/usr/bin/env python

from lambda_calculus import *

def church_to_boolean(cb):
    return cb(lambda _: True)(lambda _: False)

def church_to_int(church):
    return church(lambda x: x+1)(0)

def int_to_church(n):
    return succ(int_to_church(n-1)) if n > 0 else ZERO

def print_list(l):
    if (IS_NIL(l))(lambda _: True)(lambda _: False):
        return
    print HEAD(l)(lambda x: x+1)(0),
    return print_list(TAIL(l))

def churchlist_to_list(l):
    if (IS_NIL(l))(lambda _: True)(lambda _: False):
        return []
    return [church_to_int(HEAD(l))] + churchlist_to_list(TAIL(l))

