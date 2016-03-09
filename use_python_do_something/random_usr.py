#!/usr/bin/env python

import random

character='abcdefghijklmnopqrstuvwxyz0123456789'

a=[0]*4
a[0]=character[random.randint(0, len(character))]
a[1]=character[random.randint(0, len(character))]
a[2]=character[random.randint(0, len(character))]
a[3]=character[random.randint(0, len(character))]

name = ''.join(a);

a=[0]*6;
a[0]=character[random.randint(0, len(character))]
a[1]=character[random.randint(0, len(character))]
a[2]=character[random.randint(0, len(character))]
a[3]=character[random.randint(0, len(character))]
a[4]=character[random.randint(0, len(character))]
a[5]=character[random.randint(0, len(character))]

password=''.join(a);

f=open('a.txt', 'a')
f.write(name+','+password+'\n')
f.close();
