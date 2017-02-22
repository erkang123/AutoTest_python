#coding:utf-8
import unittest
from ddt import ddt,data,unpack
from Page.basetestcase import BaseTestCase
from Page.baidu import BaiduPage
from Page.homePage import HomePage
from model import Model

@ddt
class baiduPage(BaseTestCase,BaiduPage,HomePage):
    @data(*Model.DataHelper().readExcels())
    @unpack
    def testLogin_001(self,username,password,context_expected):
        '''测试：百度登录失败的N种情况'''
        self.doLogin(username,password)
        self.assertEqual(context_expected,self.getLoginErrorDiv())
    def testLogin_002(self):
        '''测试：百度登录成功的N种情况'''
        db = Model.DataHelper()
        self.doLogin(db.getXmlUser('login','username'),db.getXmlUser('login','password'))
        self.assertEqual(db.getXmlUser('login','niCheng'),self.getLoginErrorDiv())
if __name__=='__main__':
    unittest.main(verbosity=2)