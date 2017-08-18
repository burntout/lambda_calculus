#!/usr/bin/env python

false  = zero = lambda x: lambda y: y
true = lambda x: lambda y: x


c_not =  lambda x: x(false)(true)
c_or = lambda x: lambda y: x(true)(y(true)(false))
c_and = lambda x: lambda y: x(y(true)(false))(false)
