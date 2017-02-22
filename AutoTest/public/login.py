#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     erkang
@contact:    1226973520@qq.com
@others:     DTStudio, All rights reserved-- Created on 2017/02/16
@desc:       
"""


# 登陆
def login(self, username, password):
    driver = self.driver
    driver.find_element_by_id("idInput").clear()
    driver.find_element_by_id("idInput").send_keys(username)
    driver.find_element_by_id("pwdInput").clear()
    driver.find_element_by_id("pwdInput").send_keys(password)
    driver.find_element_by_id("loginBtn").click()


# 退出
def logout(self):
    driver = self.driver
    driver.find_element_by_link_text(u"退出").click()