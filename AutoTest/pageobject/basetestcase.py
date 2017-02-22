#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     Erkang
@contact:    1226973520@qq.com
@others:     DTStudio, All rights reserved-- Created on 2017/2/21
@desc:       封装unittest固件
"""

import unittest
from selenium import webdriver

#固件封装未类方法，可解决单次启动浏览器测试单用例问题
class BaseTestCaseClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get('http://www.baidu.com')
        cls.driver.implicitly_wait(30)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

# class BaseTestCase(unittest.TestCase):
# 	def setUp(self):
# 		self.driver=webdriver.Firefox()
# 		self.driver.maximize_window()
# 		self.driver.get('http://www.baidu.com')
# 		self.driver.implicitly_wait(30)
# 	def tearDown(self):
# 		self.driver.quit()
