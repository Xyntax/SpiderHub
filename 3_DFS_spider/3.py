# coding:utf-8
__author__ = 'xy'

from bs4 import BeautifulSoup
import urlparse
import urllib2
import time
import re
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

class DFS_spider():
    def __init__(self, domain, startpage):
        self.queue = set()
        self.visited = set()
        self.domain = domain
        self.startpage = startpage

    def page_parser(self, url):
        _queue = set()
        web = urllib2.urlopen(url, timeout=10)
        soup = BeautifulSoup(web.read())
        # 通过正则过滤合理的url(针对与freebuf.com来讲)
        tags_a = soup.findAll(name='a', attrs={'href': re.compile("^https?://")})
        try:
            for tag_a in tags_a:
                _queue.add(tag_a['href'])
        except:
            pass
        return _queue

    def DFS(self, url):
        _queue = self.page_parser(url)
        for each in _queue:
            if self.check_domain(each):
                if each not in self.visited:
                    print each
                    self.add2visited(each)
                    self.DFS(each)
            else:
                # TODO
                pass

    def check_domain(self, url):
        if self.domain in url.replace('//', '').split('/')[0]:
            return True
        else:
            return False

    def add2visited(self, url):
        self.visited.add(url)

    def _print(self):
        for each in self.visited:
            print each


if __name__ == "__main__":
    a = DFS_spider("cdxy.me", "http://www.cdxy.me")
    a.DFS("http://www.cdxy.me")
    a._print()
