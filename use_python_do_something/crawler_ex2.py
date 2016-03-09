#!/usr/bin/env python
#coding: utf-8
import urllib
from bs4 import BeautifulSoup
import re
import requests
import random

url = 'http://www.heibanke.com/lesson/crawler_ex02/'

loop = 0
success = False

while not success:
    num = random.randint(0,30)
    params = {'username':'heibanke', 'password':str(loop)}
    r = requests.post(url, data = params)
    loop +=1
    if r.text.find(u'输入的密码错误'):
        print u'输入的密码', loop, u'错误'
    else :
        print r.text
        break
print loop
