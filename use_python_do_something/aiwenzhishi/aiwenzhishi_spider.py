#!/usr/bin/env python
#coding: utf-8

import urllib
import urllib2
import re
import time
import types
import page
import mysql
import sys
from bs4 import BeautifulSoup

class Spider:

    def __init__(self):
        self.page_num = 1
        self.total_num = None
        self.page_spider = page.Page()
        self.mysql = mysql.MySql()

    def getCurrentTime(self):
        """docstring for getCurrentTime"""
        return time.strftime('[%Y-5m-%d %H:%M:%S]', time.localtime(time.time()))
             
    def getCurrentDate(self):
        """docstring for getCurrentDate"""
        return time.strftime('%Y-%m-%d', time.localtime(time.time()))

