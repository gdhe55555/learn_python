#!/usr/bin/env python

import urllib
from bs4 import BeautifulSoup
import re

websit='http://www.heibanke.com/lesson/crawler_ex00/'
html = urllib.urlopen('http://www.heibanke.com/lesson/crawler_ex00/')
bs_obj = BeautifulSoup(html, "html.parser")

#a_list = bs_obj.findAll("a")
#a_list = bs_obj.findAll("a", href=re.compile("baike\.baidu\.com\w?"))

#for aa in a_list:
#    if not aa.find("img"):
#        if aa.attrs.get('href'):
#            print aa.text ,aa.attrs['href']

a_list = bs_obj.findAll("h3")

#print a_list

text = a_list[0].text.encode('utf-8')

print(text)

ma = re.match(u"([\u4e00-\u9fa5]+)", text)
print(ma.groups())
