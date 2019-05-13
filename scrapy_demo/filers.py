#!/usr/bin/env python
# coding=UTF-8
# author: zhangjiaqi <1399622866@qq.com>
# File: filers
# Date: 5/11/2019
from scrapy.dupefilters import BaseDupeFilter, request_fingerprint
from scrapy.exceptions import DropItem


class MyDupeFilter(BaseDupeFilter):
    """
    也是五个方法;并修改settings有关filter的配置
    """

    def __init__(self):
        self.visited_fd = set()

    @classmethod
    def from_settings(cls, settings):
        return cls()

    def request_seen(self, request):
        fd = request_fingerprint(request=request)
        if fd in self.visited_fd:
            return True
        self.visited_fd.add(fd)

    def open(self):  # can return deferred
        print('开始')

    def close(self, reason):  # can return a deferred
        print('结束')


if __name__ == '__main__':
    pass
