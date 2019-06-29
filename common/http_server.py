#!/usr/bin/python
# -*- coding:utf-8 -*-
# @title : TornadoUVloopHttpServer
# @package :
# @Time : 2019-06-29 11:06 AM
# @Author : naah
# @desc :
import logging

import tornado.web
from tornado.httpserver import HTTPServer

from configuration.uvloop_configuration import TornadoUvloopConfiguration

logger = logging.getLogger(__name__)


class TornadoUVloopHttpServer(object):
    _instance = None

    __http_server = None

    @staticmethod
    def get_instance(app: tornado.Application, port: int, process_num: int = 1):
        """
        singleton class
        :param app: tornado app
        :param port: server port
        :param process_num: multi-process num,default 1
        :return:
        """
        return TornadoUVloopHttpServer(app, port, process_num)

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(TornadoUVloopHttpServer, cls).__new__(cls)
            cls._instance.__init(args[0], args[1], args[2])
        return cls._instance

    @classmethod
    def __init(cls, app: tornado.Application, port: int, process_num: int):
        cls.__http_server = HTTPServer(app)
        cls.__http_server.bind(port)
        cls.__process_num = process_num
        logger.info("http server bind port:%d ,process_num:%d", port, process_num)

    def start(cls):

        tornado.ioloop.IOLoop.configure(TornadoUvloopConfiguration)
        cls.__http_server.start(cls.__process_num)
        tornado.ioloop.IOLoop.current().start()
