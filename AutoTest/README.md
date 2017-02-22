

1.目录结构
/demo_html      演示用的html页面          【实际项目中，请删除！】
/pageobject     PO模式的例子
/public         公共类。 HTMLTestRunner.py是重点，不要轻易修改！
/report         存放测试报告
/test_case      测试用例
    --/common   Selenium常用API的讲解！   【实际项目中，请删除！】
/test_data      测试数据
.all_test.py | all_test_send_report.py 框架运行入口

1.1 /test_case目录下的脚本说明
/test_case/test_00_find_element.py   介绍元素定位的8种方法
/test_case/test_01_open_baidu.py 	入门的测试用例
/test_case/test_02_login_126mail.py	    流水式的脚本
/test_case/test_03_login_via_function.py  将login登陆动作抽象出来，这里使用了函数
/test_case/test_04_login_via_xml.py  将登陆的账号密码参数化，所谓的数据驱动
/test_case/test_05_config_firefox.py    定制Firefox浏览器

/test_data/login.xml    存放test_04_login_via_xml测试登录功能的测试数据
/test_data/test.html    用来演示元素定位的html文件



2.学习顺序
2.1 先学习 /test_case/common 目录下的每一个用例，按照编号顺序，了解常用 Selenium API 的用法；
2.2 学习 Python unittest 的基本用法；（找度娘）
2.3 学习 all_test.py 如何运行所有的用例，以及 all_test_send_report.py 如何发送邮件；
2.4 学习 /test_case 根目录下的项目用例。（如果不了解 python unittest的用法，请自行学习unittest的基本用法）；
2.5 学习 /public/HTMLTestRunner.py ，了解Runner的结构；