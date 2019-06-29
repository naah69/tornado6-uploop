#!/usr/bin/python
# -*- coding:utf-8 -*-
# @title : TornadoUvloopConfiguration
# @package :
# @Time : 2019-06-29 11:06 AM
# @Author : naah
# @desc :
import asyncio
import logging

import uvloop
from tornado.platform.asyncio import BaseAsyncIOLoop

logger = logging.getLogger(__name__)


# uvloop配置

class TornadoUvloopConfiguration(BaseAsyncIOLoop):

    def initialize(self, **kwargs):
        logger.info("uvloop will init ")
        asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
        loop = uvloop.new_event_loop()
        try:
            super(TornadoUvloopConfiguration, self).initialize(
                loop, close_loop=True, **kwargs)
        except Exception:
            loop.close()
            raise
