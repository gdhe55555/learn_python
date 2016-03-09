#!/usr/bin/env python

import urllib
from bs4 import BeautifulSoup
import re

html = urllib.urlopen('http://baike.baidu.com/view/284853.htm')
bs_obj = BeautifulSoup(html, "html.parser")

#a_list = bs_obj.findAll("a")
a_list = bs_obj.findAll("a", href=re.compile("baike\.baidu\.com\w?"))

for aa in a_list:
    if not aa.find("img"):
        if aa.attrs.get('href'):
            print aa.text ,aa.attrs['href']


