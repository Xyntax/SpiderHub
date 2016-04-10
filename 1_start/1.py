# -*- coding: utf-8 -*-

__author__ = 'xy'

from bs4 import BeautifulSoup
import urllib
import re
# 解析url
import urlparse

web = urllib.urlopen("http://www.freebuf.com")
soup = BeautifulSoup(web.read())
# 寻找name属性为a, href属性符合后面正则的
tags_a = soup.findAll(name="a", attrs={'href': re.compile("^https?://")})
# print tags_a

# set创建集合，直接可剔除重复
url = set()
for each in tags_a:
    url.add(each["href"])

for each in url:
    print each
    o = urlparse.urlparse(each)
    print o
