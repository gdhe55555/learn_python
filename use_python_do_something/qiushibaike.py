#!/usr/bin/env python
#coding: utf-8

import urllib
import urllib2
import re

page = 1
url = 'http://www.qiushibaike.com/hot/page' + str(page)
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
headers = {'User-Agent':user_agent}
try:
    request = urllib2.Request(url, headers = headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    pattern = re.compile('<div.*?author(.*?)">.*?<a.*?<img.*?>.*?</a>.*?<h2>(.*?)</h2>.*?</a>.*?<div.*?'+
            'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>', re.S)
    items = re.findall(pattern, content)
    for item in items:
        havaImg = re.search('img', item[4])
        if not havaImg:
            print item[0],item[1],item[2], item[3],item[5]
except urllib2.URLError, e:
    if hasattr(e, 'code'):
        print e.code
    if hasattr(e, 'reason'):
        print e.reason

