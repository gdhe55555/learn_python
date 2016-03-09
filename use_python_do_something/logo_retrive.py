#!/usr/bin/env python
#coding: utf-8

import urllib
from bs4 import BeautifulSoup

url='http://www.heibanke.com'

html = urllib.urlopen(url)
bs_obj = BeautifulSoup(html, 'html.parser')

imageLocation = bs_obj.find('img')['src']
print imageLocation

urllib.urlretrieve(url+imageLocation, 'logo.png')
