#!/usr/bin/env python
#coding: utf-8

import urllib
import urllib2
import re
import time
import types 
import tool
from bs4 import BeautifulSoup

class Page:
    def __init__(self):
        self.tool = tool.Tool()

    def getCurrentTime(self):
        """docstring for getCurrentTime"""
        return time.strftime('[%Y-5m-%d %H:%M:%S]', time.localtime(time.time()))
             
    def getCurrentDate(self):
        """docstring for getCurrentDate"""
        return time.strftime('%Y-%m-%d', time.localtime(time.time()))
    
    def getPageByURL(self, url):
        """docstring for getPageByURL"""
        try:
            request = urllib2.Request(url)
            response = urllib2.urlopen(requests)
            return response.read().decode('utf-8')
        except urllib2.URLError,e:
            pass
