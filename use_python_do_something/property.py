#!/usr/bin/env python

class Car(object):
    """class Car"""
    country = 'china'
    def __init__(self, length, width, height, owner=None):
        self.owner = owner
        self.length, width, height, owner = length, width, height, owner

if __name__ == '__main__':
    a = Car(1.1, 1.2, 1.3, u'black')
    print a.owner
    print a.country
    print a

    b = Car(1.3, 1.3, 1.2, u'white')
    print b.country
    print Car.country

    print '---------------------------'
    b.country = 'america'
    print a.country + ' '+ Car.country + '\n'

    del a.country
    print a.country

        
