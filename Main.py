#!/usr/bin/python
# -*- coding:utf-8 -*-
from tornado.web import Application

from common.http_server import TornadoUVloopHttpServer
from handler.hello_handler import HelloHandler


class Main(Application):
    def __init__(self, **settings):
        super(Main, self).__init__([("/", HelloHandler)], **settings)


if __name__ == '__main__':
    TornadoUVloopHttpServer.get_instance(Main(), 6969).start()
