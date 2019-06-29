#!/usr/bin/python
# -*- coding:utf-8 -*-
# @title : HelloHandler
# @package :
# @Time : 2019-06-29 11:06 AM
# @Author : naah
# @desc :
from tornado import gen


class HelloHandler(object):
    @gen.coroutine
    def get(self):
        self.write("Hello, world")
