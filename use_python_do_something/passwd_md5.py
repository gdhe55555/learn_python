#!/usr/bin/env python

f=open('a.txt', 'r')
name_password=f.readline().strip().split(',')
f.close();

import hashlib
passwd_md5=hashlib.md5(name_password[1]).hexdigest()

f=open('a_md5.txt', 'a')
f.write(name_password[0]+','+passwd_md5);
f.close();
