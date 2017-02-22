#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     erkang
@contact:    1226973520@qq.com
@others:     DTStudio, All rights reserved-- Created on 2017/2/20
@desc:       页面元素定位，此为示列页面
"""
from selenium.webdriver.common.by import By
from pageobject.BasePage import Page
'''百度登录验证'''
class BaiduPage(Page):
    click_loc = (By.XPATH,".//*[@id='u1']/a[7]")
    userName_loc = (By.ID,'TANGRAM__PSP_8__userName')
    passWord_loc = (By.ID,'TANGRAM__PSP_8__password')
    clickButton_loc = (By.ID,'TANGRAM__PSP_8__submit')
    error_loc = (By.ID,'TANGRAM__PSP_8__error')
    closelogin = (By.ID,'TANGRAM__PSP_2__closeBtn')
    clearbtn = (By.ID,'TANGRAM__PSP_8__userName_clearbtn')
    def click(self):
        self.wait
        self.find_element(*self.click_loc).click()
    def clearButton(self):
        self.wait
        self.find_element(*self.userName_loc).clear()
    def getUserTextField(self,username):
        self.wait
        self.find_element(*self.userName_loc).send_keys(username)
    def getPasswordField(self,password):
        self.wait
        self.find_element(*self.passWord_loc).send_keys(password)
    def getSubmitButton(self):
        self.wait
        self.find_element(*self.clickButton_loc).click()
    def getLoginErrorDiv(self):
        self.wait
        return self.find_element(*self.error_loc).text
    def closeLogin(self):
        self.wait
        self.find_element(*self.closelogin).click()
    def login(self,username,password):
        self.doLogin(username,password)
        # return HomePage(self.driver)
    def doLogin(self,username,password):
        self.click()
        self.clearButton()
        self.getUserTextField(username)
        self.getPasswordField(password)
        self.getSubmitButton()