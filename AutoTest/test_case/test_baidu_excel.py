import unittest

from Page import basetestcase
from Page import baidu
from model import Model


class baiduPage(basetestcase.BaseTestCase, baidu.Baidu, Model.DataHelper):
    def test_001(self):
        '''验证:用户名密码都为空,点击登录返回的错误信息'''
        self.login(self.readExcel(1,0),self.readExcel(1,1))
        self.assertEqual(self.readExcel(1,2),self.getErrorText())
    def test_002(self):
        '''验证:密码为空,点击登录返回的错误信息'''
        self.login(self.readExcel(2, 0), self.readExcel(2, 1))
        self.assertEqual(self.readExcel(2, 2), self.getErrorText())
    def test_003(self):
        '''验证:验证码输入为空，点击登录返回的错误信息'''
        self.login(self.readExcel(3, 0), self.readExcel(3, 1))
        self.assertEqual(self.readExcel(3, 2), self.getErrorText())

if __name__ == '__main__':
    unittest.main(verbosity=2)