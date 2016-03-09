#!/usr/bin/env python
#coding: utf-8

import urllib
import urllib2
import re
import os

class Spider:

    def __init__(self):
        self.siteURL = 'http://mm.taobao.com/json/request_top_list.htm'

    def getPage(self,pageIndex):
        url = self.siteURL + "?page=" + str(pageIndex)
        print url
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        return response.read().decode('gbk')

    def getContents(self,pageIndex):
        page = self.getPage(pageIndex)
        pattern = re.compile('<div class="list-item".*?pic-word.*?<a href="(.*?)".*?<img src="(.*?)".*?<a class="lady-name.*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>',re.S)
        items = re.findall(pattern,page)
        for item in items:
            print item[0],item[1],item[2],item[3],item[4]
            
    def saveImg(self, imageURL, fileName):
        """docstring for saveImg"""
        u = urllib.urlopen(imageURL)
        data = u.read()
        f = open(fileName, 'wb')
        f.write(data)
        f.close()

    def saveBrief(self, content, name):
        """docstring for saveBrief"""
        fileName = name + '/' + name + '.txt'
        f = open(fileName, 'w+')
        print u'正在偷偷的保存他的个人信息', fileName
        f.write(content.encode('utf-8'))

    def mkdir(self, path):
        """path mkdir"""
        path = path.strip()
        isExists = os.path.exists(path)
        if not isExists:
            os.mkdir(path)
            return True
        else:
            return False


spider = Spider()
spider.getContents(1)

