#coding:utf-8
import unittest

from ddt import ddt,data,unpack
from Page.baidu import BaiduPage
from model import Model
from Page.basetestcase import BaseTestCase


@ddt
class baiduPage(BaseTestCase,BaiduPage):

    @data(*Model.DataHelper().getlist)
    @unpack
    def test_FailLogin(self,value1,value2,expected):
        self.login(value1,value2)
        print('getError',self.getLoginErrorDiv(),'end')
        self.assertEqual(self.getLoginErrorDiv(),expected)

if __name__=='__main__':
    unittest.main(verbosity=2)