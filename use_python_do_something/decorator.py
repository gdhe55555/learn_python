#!/usr/bin/env python

def decorator(f):
    print "before "+f.__name__+" called"
    return f

def myfunc1():
    """myfunc1 called"""
    print "myfunc1() called"

@decorator
def myfunc2():
    """myfunc2"""
    print "myfunc2() called"


if __name__=="__main__":
   # pass
    decorator(myfunc1)()
    myfunc2()
