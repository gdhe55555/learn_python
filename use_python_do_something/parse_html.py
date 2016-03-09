#!/usr/bin/env python

from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):
    in_title=False
    in_loca =False
    in_time =False

    def handle_starttag(self, tag, attrs):
        """handle_starttag"""
        if('class', 'event-title') in attrs:
            self.in_title = True
        elif('class', 'event-location') in attrs:
            self.in_loca = True
        elif tag == 'time':
            self.in_time = True
            self.times=[]

    def handle_data(self, data):
        """handle_data"""
        if self.in_title:
            print('-'*50)
            print('Title:' + data.strip())
        if self.in_loca:
            print('Location:' + data.strip())
        if self.in_time:
            self.times.append(data)

    def handle_endtag(self, tag):
        if tag == 'h3':self.in_title = False
        if tag == 'span':self.in_loca = False
        if tag == 'time':
            self.in_time = False
            print('Time:'+''.join(self.times))


parser = MyHTMLParser()
with open('index.html') as html:
    parser.feed(html.read())
