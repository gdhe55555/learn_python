#!/usr/bin/env python
#coding: utf-8
import urllib
from selenium import webdriver
from bs4 import BeautifulSoup
import re
import requests
import random
import time

url = 'http://www.heibanke.com/lesson/crawler_ex01/'


driver = webdriver.Firefox()
loop = 0
success = False

while not success:
    driver.get(url)
    time.sleep(1)
    num = random.randint(0,30)
    driver.find_element_by_name('username').send_keys('heibanke')
    driver.find_element_by_name('password').send_keys(str(num))
    driver.find_element_by_id('id_submit').click()

    html = driver.page_source
    #params = {'username':'heibanke', 'password':str(loop)}
    #r = requests.post(url, data = params)
    bs_obj = BeautifulSoup(html)
    loop +=1
    if bs_obj.text.find(u'输入的密码错误'):
        print u'输入的密码', loop, u'错误'
    else :
        print bs_obj.text
        break
print loop
