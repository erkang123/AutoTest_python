#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     erkang
@contact:   1226973520@qq.com
@others:     DTStudio, All rights reserved-- Created on 2017/02/17
@desc:       
"""
import unittest
import os
import sys
import time
import smtplib
from email.mime.text import MIMEText
# from public import HTMLTestRunner
import HTMLTestRunner

def send_mail(file_new):
    # 发件人邮箱
    mail_from = '2663784398@qq.com'
    # 收件人邮箱
    mail_to = 'sz_yonkan@163.com'
    # 定义正文
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    msg = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    # 定义标题
    msg['Subject'] = u"自动化测试报告"
    # 定义发送时间（不定义的可能有的邮件客户端会不显示发送时间）
    msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
    smtp = smtplib.SMTP()
    # 连接 SMTP 服务器，此处用的 126 的 SMTP 服务器
    smtp.connect('smtp.qq.com')
    # 发件人的用户名密码
    smtp.login('2663784398@qq.com', 'he1226973520')
    smtp.sendmail(mail_from, mail_to, msg.as_string())
    smtp.quit()
    print('email has send out !')


# ======查找测试报告目录，找到最新生成的测试报告文件====
def send_report(report_folder):
    result_dir = report_folder
    lists = os.listdir(result_dir)
    lists.sort(key=lambda fn: os.path.getmtime(result_dir + "\\" + fn))
    # print (u'最新测试生成的报告： '+lists[-1])
    # 找到最新生成的文件
    file_new = os.path.join(result_dir, lists[-1])
    print(file_new)
    # 调用发邮件模块
    send_mail(file_new)

def suite():
    # 定义测试文件查找的目录
    test_dir = os.path.abspath(os.path.dirname(__file__)) + os.sep + 'test_case'
    dir_case=unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py',top_level_dir=None)
    return dir_case
#获取当前时间
def getNowTime():
    return time.strftime("%Y-%m-%d %H_%M_%S",time.localtime(time.time()))
def runAutomation():
    #定义查找报告目录
    report_folder = os.path.abspath(os.path.dirname(__file__)) + os.sep + 'report'
    filename=report_folder+getNowTime()+'TestReport.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'自动化测试报告',description=u'自动化测试报告详细的信息')
    runner.run(suite())
    fp.close()  # 关闭生成的报告
    # send_report(report_folder)  # 发送报告
if __name__=='__main__':
    runAutomation()

# def gen_test_suite():
#     testunit = unittest.TestSuite()
#     # 定义测试文件查找的目录
#     test_dir = os.path.abspath(os.path.dirname(__file__)) + os.sep + 'test_case'
#     # 注意：pattern，用来匹配/test_case目录下哪些用例加入本次运行
#     discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py',
#                                                    top_level_dir=None)
#     # discover 方法筛选出来的用例，循环添加到测试套件中
#     for test_suite in discover:
#         for test_case in test_suite:
#             testunit.addTests(test_case)
#             print(testunit)
#     return testunit
#
#
# if __name__ == '__main__':
#     # 将项目的目录加载到系统变量中
#     cur_dir = os.getcwd()
#     sys.path.append(cur_dir)
#     now = time.strftime("%Y-%m-%d %H_%M_%S")
#
#     os.environ['WEBSERVICE_ITERATION_RUN_TIME'] = now
#
#     report_folder = cur_dir + os.sep + 'report' + os.sep
#     filename = report_folder + now + '_result.html'  # 测试报告的路径名
#     fp = open(filename, 'wb')
#     runner = HTMLTestRunner.HTMLTestRunner(
#         stream=fp,
#         title=u'项目自动化测试报告',
#         description=u'用例执行情况：',
#         )
#     all_test_units = gen_test_suite()
#     runner.run(all_test_units)
#     fp.close()  # 关闭生成的报告
#     send_report(report_folder)  # 发送报告
#
#     # 此文件和 all_test.py的区别在于，多了一步：send_report(test_report)
