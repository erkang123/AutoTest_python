#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     Erkang
@contact:    1226973520@qq.com
@others:     DTStudio, All rights reserved-- Created on 2017/2/20
@desc:		 PO模式，所有页面定位的基类
"""

import  time as t
from selenium.webdriver.support.expected_conditions import NoSuchElementException

class Page(object):
    """
    基类，用于所有页面继承
    """
    homepage = 'http://www.baidu.com'
    def __init__(self,driver,base_url = homepage,parent = None):
        self.base_url = base_url
        self.driver = driver
        # self.timeout = 30
        # self.parent = parent
        # self.tabs = {}
    def _open(self,url):
        url_o = self.base_url+url
        self.driver.get(url_o)
        assert self.on_page(url),'Did not land on %s'%url_o

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    def open(self,url):
        self._open(url)

    def on_page(self,url):
        return self.driver.current_url == (self.base_url + url)

    def script(self, src):
        return self.driver.execute_script(src)

    def send_keys(self, loc, value, clear_first=True, click_first=True):
        try:
            loc = getattr(self, '_%s' % loc)
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
            self.find_element(*loc).send_keys(value)
        except AttributeError:
            print('%s page does not have "%s" locator' % (self, loc))

    def find_element(self, *loc):
        try:
            return self.driver.find_element(*loc)
        except (NoSuchElementException, KeyError, ValueError, Exception) as e:
            print('Error details:%s' % (e.args[0]))

    @property
    def wait(self):
        t.sleep(2)














