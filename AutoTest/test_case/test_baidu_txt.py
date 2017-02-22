import unittest

from Page import basetestcase
from Page import baidu
from model import Model


class baiduPage(basetestcase.BaseTestCase, baidu.Baidu, Model.DataHelper):
    def test_001(self):
        '''验证:用户名密码都为空,点击登录返回的错误信息'''
        self.login(self.readFile(0),self.readFile(0))
        self.assertEqual('请您填写手机/邮箱/用户名',self.getErrorText())
    def test_002(self):
        '''验证:密码为空,点击登录返回的错误信息'''
        self.login(self.readFile(1), self.readFile(0))
        self.assertEqual('请您填写密码', self.getErrorText())
    def test_003(self):
        '''验证:验证码输入为空，点击登录返回的错误信息'''
        self.login(self.readFile(1), self.readFile(1))
        self.assertEqual('请您填写验证码', self.getErrorText())

if __name__ == '__main__':
    unittest.main(verbosity=2)