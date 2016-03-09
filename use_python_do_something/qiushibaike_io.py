#!/usr/bin/env python
#coding: utf-8

import urllib
import urllib2
import re
import thread
import time

#糗事百科爬虫类
class QSBK(object):
    """docstring for QSBK"""
    def __init__(self):
       self.pageIndex = 1
       #初始化headers
       self.user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
       self.headers = {'User-agent':self.user_agent}
       #存放段子的变量
       self.stories = []
       #存放程序是否是否继续运行的变量
       self.enable = False

    def getPage(self, pageIndex):
        """getPage"""
        try:
            url = 'http://www.qiushibaike.com/hot/page' + str(pageIndex)
            request = urllib2.Request(url, headers = self.headers)
            response = urllib2.urlopen(request)
            content = response.read().decode('utf-8')
            return content
        except urllib2.URLError, e:
            if hasattr(e, 'reason'):
                print u'糗事百科失败，错误原因', e.reason
                return None
    
    def getPageItems(self, pageIndex):
        """docstring for getPageItems"""
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print u'页面加载失败...'
            return None
        pattern = re.compile('<div.*?author.*?">.*?<a.*?<img.*?>.*?</a>.*?<h2>(.*?)</h2>.*?</a>.*?<div.*?'+
                'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>', re.S)
        items = re.findall(pattern, pageCode)
        pageStories = []
        for item in items:
            havaImg = re.search('img', item[3])
            if not havaImg:
                replaceBR = re.compile('<br/>')
                text = re.sub(replaceBR, '\n', item[1])
                pageStories.append([item[0].strip(),text.strip(),item[2].strip(),item[4].strip()])
        return pageStories

    def loadPage(self):
        """docstring for loadPage"""
        if self.enable == True:
            if len(self.stories) < 2:
                pageStories = self.getPageItems(self.pageIndex)
                if pageStories:
                    self.stories.append(pageStories)
                    self.pageIndex += 1
            print 'load page success!'

    def getOneStroy(self, pageStories, page):
        """docstring for getOneStroy"""
        for story in pageStories:
            input = raw_input()
            self.loadPage()
            if input == 'Q':
                self.enable = False
                return
            print u'第%d页\t发布人:%s\t发布时间:%s\t赞:%s\n%s' %(page, story[0], story[2], story[3], story[1])

    def start(self):
        """docstring for start"""
        print u'正在读取糗事百科，按回车查看新段子，Q退出'
        self.enable = True
        self.loadPage()
        nowPage= 0
        while self.enable:
            if len(self.stories) > 0:
                pageStories = self.stories[0]
                nowPage += 1
                del self.stories[0]
                self.getOneStroy(pageStories, nowPage)

if __name__ == '__main__':
    spider = QSBK()
    print '-----'*10

    spider.start()
