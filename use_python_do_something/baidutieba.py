#!/usr/bin/env python
#coding: utf-8

import urllib
import urllib2
import re

class Tool(object):
    """docstring for Tool"""
    removeImg = re.compile('<img.*?>| {7}')
    removeAddr = re.compile('<a.*?>|</a>')
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    replaceTD = re.compile('<td>')
    replacePara = re.compile('<p.*?>')
    replaceBR = re.compile('<br><br>|<br>')
    removeExtraTag = re.compile('<.*?>')

    def replace(self, x):
        """docstring for replace"""
        x = re.sub(self.removeImg, "", x)
        x = re.sub(self.removeAddr, "", x)
        x = re.sub(self.replaceLine, '\n', x)
        x = re.sub(self.replaceTD, '\t', x)
        x = re.sub(self.replacePara, '\n   ', x)
        x = re.sub(self.replaceBR, '\n', x)
        x = re.sub(self.removeExtraTag, '', x)
        return x.strip()

        

class BDTB(object):
    """docstring for BDTB"""
    def __init__(self, baseUrl, seeLZ, floorTag):
        self.baseURL = baseUrl
        self.seeLZ = '?see_lz=' + str(seeLZ)
        self.tool = Tool()
        self.file = None
        self.floor = 1
        self.defaultTitle = u'百度贴吧'
        self.floorTag = floorTag

    def getPage(self, pageNum):
        try:
            url = self.baseURL + self.seeLZ + '&pn=' + str(pageNum)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            #print response.read()
            content = response.read().decode('utf-8')                                                                                       
            return content
        except urllib2.URLError, e:
            if hasattr(e, 'reason'):
                print u'连接百度贴吧失败，错误原因', e.reason
                return None

    def getTitle(self):
        """docstring for getTitle"""
        page = self.getPage(1)
        pattern = re.compile('<h\d class="core_title_txt.*?>(.*?)</h\d>', re.S)
        result = re.search(pattern, page)
        if result:
            return result.group(1).strip()
        else:
            return None

    def getPageNum(self):
        """docstring for getPageNum"""
        page = self.getPage(1)
        pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>',re.S)
        result = re.search(pattern, page)
        if result:
            return result.group(1).strip()
        else:
            return None
    def getContent(self, page):
        """docstring for getContent"""
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>', re.S)
        items = re.findall(pattern, page)
        contents = []
        for item in items:
        #    print item
        #    print floor, u'楼', '-----'*20, '\n'
        #    print self.tool.replace(item)
            content = '\n' + self.tool.replace(item) + '\n'
            contents.append(content.encode('utf-8'))
        return contents

    def setFileTitle(self, title):
        """docstring for setFileTitle"""
        if title is not None:
            self.file = open(title + '.txt', 'w+')
        else:
            self.file = open(self.defaultTitle + '.txt', 'w+')

    def writeData(self, contents):
        """docstring for writeData"""
        for item in contents:
            if self.floorTag == '1':
                floorLine = '\n' + str(self.floor) + u'-----'*20 + '\n'
                self.file.write(floorLine)
            self.file.write(item)
            self.floor += 1

    def start(self):
        """docstring for start"""
        indexPage = self.getPage(1)
        pageNum = self.getPageNum()
        title = self.getTitle()
        self.setFileTitle(title)
        if pageNum == None:
            print u'URL失效，请重试'
            return 
        try:
            print u'该贴共有' + str(pageNum) + u'页'
            for i in range(1, int(pageNum)+1):
                print u'正在写入第' + str(i) + u'页数据'
                page = self.getPage(i)
                contents = self.getContent(page)
                self.writeData(contents)
        except IOError, e:
            print u'写入异常，原因' + e.message
        finally:
            print u'写入任务成功'



if __name__ == '__main__':
    print u'请输入帖子代号'
    baseURL = 'http://tieba.baidu.com/p/' + str(raw_input(u'http://tieba.baidu.com/p/'))
    seeLZ = raw_input("是否只获取楼主发言，是输入1，否输入0\n")
    floorTag = raw_input("是否写入楼层信息，是输入1，否输入0\n")
    bdtb = BDTB(baseURL, seeLZ, floorTag)
    bdtb.start()
