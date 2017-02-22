import unittest

from Page import basetestcase
from Page import baidu
from model import Model


class baiduPage(basetestcase.BaseTestCase, baidu.Baidu, Model.DataHelper):
    def test_001(self):
        '''验证:用户名密码都为空,点击登录返回的错误信息'''
        self.login(self.getXmlUser('faillogin1','username'),self.getXmlUser('faillogin1','password'))
        self.assertEqual(self.getXmlUser('faillogin1','expected'),self.getErrorText())
    def test_002(self):
        '''验证:密码为空,点击登录返回的错误信息'''
        self.login(self.getXmlUser('faillogin2', 'username'), self.getXmlUser('faillogin2', 'password'))
        self.assertEqual(self.getXmlUser('faillogin2', 'expected'), self.getErrorText())
    def test_003(self):
        '''验证:验证码输入为空，点击登录返回的错误信息'''
        self.login(self.getXmlUser('faillogin3', 'username'), self.getXmlUser('faillogin3', 'password'))
        self.assertEqual(self.getXmlUser('faillogin3', 'expected'), self.getErrorText())

if __name__ == '__main__':
    unittest.main(verbosity=2)