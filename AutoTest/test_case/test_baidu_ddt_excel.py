#coding:utf-8
import unittest

from ddt import ddt,data,unpack
from Page.basetestcase import BaseTestCase
from Page.baidu import BaiduPage
from model import Model


@ddt
class baiduPage(BaseTestCase,BaiduPage):
    @data(*Model.DataHelper().readExcels())
    @unpack
    def test_FailLogin(self,value1,value2,expected):
        self.login(value1,value2)
        self.assertEqual(self.getLoginErrorDiv(),expected)
if __name__=='__main__':
    unittest.main(verbosity=3)