import unittest
from model.Model import DataHelper
from Page.basetestcase import BaseTestCase
from Page.baidu import BaiduPage


class baiduPage(BaseTestCase,DataHelper,BaiduPage):

    def test_001(self):
        '''验证:用户名密码都为空,点击登录返回的错误信息'''
        self.login('','')
        self.assertEqual(self.getLoginErrorDiv(),'请您填写手机/邮箱/用户名')
        self.closeLogin()
    def test_002(self):
        '''验证:密码为空,点击登录返回的错误信息'''
        self.login('13434482994', '')
        self.assertEqual(self.getLoginErrorDiv(), '请您填写密码')
        self.closeLogin()
    def test_003(self):
        '''验证:验证码输入为空，点击登录返回的错误信息'''
        self.login('13434482994', 'admin')
        self.assertEqual(self.getLoginErrorDiv(), '请您填写验证码')
        self.closeLogin()

#     @staticmethod
#     def suite(self):
#         # suite = unittest.TestSuite(unittest.makeSuite(baiduPage))
#         suite = unittest.TestLoader().loadTestsFromTestCase(baiduPage)
#         return suite
# if __name__ == '__main__':
#     unittest.TextTestRunner(verbosity=3).run(baiduPage.suite())

# if __name__ == '__main__':
#     # suite = unittest.TestSuite()
#     # suite.addTest(baiduPage('test_001'))
#     # suite.addTest(baiduPage('test_002'))
#     # suite.addTest(baiduPage('test_003'))
#
#     suite = unittest.TestSuite(unittest.makeSuite(baiduPage))
#     unittest.TextTestRunner(verbosity=3).run(suite)
if __name__ == '__main__':
    unittest.main(verbosity=3)