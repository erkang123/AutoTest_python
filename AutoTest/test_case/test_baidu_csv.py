import unittest
from Page import baidu
from model import Model
from Page import basetestcase


class baiduPage(basetestcase.BaseTestCase,Model.DataHelper,baidu.Baidu):
    def test_001(self):
        '''验证:用户名密码都为空,点击登录返回的错误信息'''
        self.login(self.readCsv(0,0),self.readCsv(0,1))
        self.assertEqual(self.readCsv(0,2),self.getErrorText())
    def test_002(self):
        '''验证:密码为空,点击登录返回的错误信息'''
        self.login(self.readCsv(1, 0), self.readCsv(0, 1))
        self.assertEqual(self.readCsv(1, 2), self.getErrorText())
    def test_003(self):
        '''验证:验证码输入为空，点击登录返回的错误信息'''
        self.login(self.readCsv(3, 0), self.readCsv(3, 1))
        self.assertEqual(self.readCsv(3, 2), self.getErrorText())

if __name__ == '__main__':
    unittest.main(verbosity=2)