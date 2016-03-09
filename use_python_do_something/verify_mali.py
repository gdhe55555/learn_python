#!/usr/bin/env python

import re

def fun1(email):
    """verify email"""
    print(re.match(r'^([0-9a-zA-Z\.\s]+)@(\w+)(\.com|\.org)', email).groups())


fun1('someone@gmali.com')
fun1('bill gates @microsoft.com')

def fun2(email):
    """verify email"""
    m = re.match(r'^<([0-9a-zA-Z\.\s]+)>\s*(.+)$', email)
    if m:
        print(m.group(1), end='')
        fun1(m.group(2))
    else:
        fun1(email)

fun2('<TOm Paris> tom@voyager.org')
fun2('someoneone@gmali.com')
