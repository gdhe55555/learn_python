#!/usr/bin/env python

def Howdy(self, you):
    print("Howdy," + you)

Mylist = type("Mylist", (list,), dict(x= 23, Howdy=Howdy))

m1 = Mylist()
m1.append("Camemebert")
print(m1)
print(m1.x)
m1.Howdy("John")
