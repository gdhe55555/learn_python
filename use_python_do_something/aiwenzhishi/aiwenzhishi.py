#!/usr/bin/env python

import time
import urllib2
import urllib
from bs4 import BeautifulSoup
import re

def getCurrentTime(self):
    """docstring for getCurrentTime"""
    return time.strftime('[%Y-5m-%d %H:%M:%S]', time.localtime(time.time()))

def getCurrentDate(self):
    """docstring for getCurrentDate"""
    return time.strftime('%Y-%m-%d', time.localtime(time.time()))


def main(self):
    """docstring for main"""
    f_handler = open('out.log', 'w')
    sys.stdout = f_handler
    page = open('page.txt', 'r')
    content = page.readline()
    start_page = int(content.strip()) - 1
    page.close()
    print self.getCurrentTime(), u'开始页码', start_page
    print self.getCurrentTime(). u'爬虫正在启动，开始爬取爱问知识人问题'
    self.total_num = self.getTotalPageNum()
    print self.getCurrentTime(), '获取到目录页码个数', self.total_num, '个'
    if not start_page:
        start_page = self.total_num
    for x in range(1, start_page):
        print self.getCurrentTime(), '正在抓取第', start_page-x+1, '个页面'
        try:
            self.getQuestions(start_page-x+1)
        except urllib2.URLError, e :
            if hasattr(e, 'reason'):
                print self.getCurrentTime(),"某总页面内抓取或提取失败,错误原因", e.reason
        except Exception, e:
                print self.getCurrentTime(),"某总页面内抓取或提取失败,错误原因:",e

        if start_page-x+1 < start_page:
            f = open('page.txt', 'w')
            f.write(str(start_page-x+1))
            print self.getCurrentTime(),"写入新页码",start_page-x+1
            f.close()

