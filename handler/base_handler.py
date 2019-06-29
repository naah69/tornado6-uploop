#!/usr/bin/python
# -*- coding:utf-8 -*-
# @title : BaseHandler
# @package :
# @Time : 2019-06-29 11:06 AM
# @Author : naah
# @desc :
from tornado.web import RequestHandler


# 抽象类
class BaseHandler(RequestHandler):
    # 重写访问日志
    def _request_summary(self):
        return "{} {} ({}@{})".format(self.request.method, self.request.uri,
                                      self.request.body.decode('utf-8', 'strict').replace("\n", "").replace(" ", ""),
                                      self.request.remote_ip)
        pass
