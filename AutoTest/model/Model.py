#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     erkang
@contact:    1226973520@qq.com
@others:     DTStudio, All rights reserved-- Created on 2017/2/20
@desc:       操作各种数据
"""
import os,platform,csv,xlrd,xml.dom.minidom,pymysql
from model import config
import sqlite3
class Config(object):
    def __init__(self):
        pass
    # 设置数据路径
    @staticmethod
    def data_dirs():
        if platform.system() == 'Windows':
            BASE_DIR = '\\'.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))).split('\\'))
            data_path = os.path.join(BASE_DIR, 'test_data')
        else:
            BASE_DIR = '/'.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))).split('/'))
            data_path = os.path.join(BASE_DIR, 'test_data')
        return data_path
class DataHelper(object):
    def __init__(self):
        pass
    # 读取txt格式文件内容
    def readFile(self,index):
        with open(Config.data_dirs() + '/system.txt', 'r') as f:
            readfile = f.readlines()
        return readfile[index]

    # 读取cvs格式文件内容
    def readCsv(self,rowValue,colValue):
        rows = []
        with open(Config.data_dirs() + '/system.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader, None)
            for row in reader:
                rows.append(row)
        return ''.join(rows[rowValue][colValue])
    #读取excel表数据
    def readExcel(self,rowValue,colValue):
        book = xlrd.open_workbook(Config.data_dirs()+'/system.xlsx')
        sheet = book.sheet_by_index(0)
        return sheet.cell_value(rowValue,colValue)
    #读取excel表下sheet所有数据
    def readExcels(self):
        rows = []
        book = xlrd.open_workbook(Config.data_dirs() + '/system.xlsx')
        sheet = book.sheet_by_index(0)
        for row in range(1,sheet.nrows):
            rows.append(list(sheet.row_values(row,0,sheet.ncols)))
        return rows

    #获取xml数据
    # 获取节点
    def getXmlData(self,value):
        # 打开文档
        dom = xml.dom.minidom.parse(Config.data_dirs() + "/system.xml")
        # 得到文档元素的结构
        db = dom.documentElement
        name = db.getElementsByTagName(value)
        nameValue = name[0]
        return nameValue.firstChild.data
    # 获取节点里的数据
    def getXmlUser(self,parent, child):
        dom = xml.dom.minidom.parse(Config.data_dirs() + "/system.xml")
        db = dom.documentElement
        itemlist = db.getElementsByTagName(parent)
        item = itemlist[0]
        return item.getAttribute(child)

    # ddt获取数据
    @property
    def getlist(self):
        list = (['', '', '请您填写手机/邮箱/用户名'],
                ['13434482994', '', '请您填写密码'],
                ['', 'admin', '请您填写手机/邮箱/用户名'],
                ['13434482994', 'admin', '请您填写验证码'])
        return list
class MySQLHelper(object):
    def __init__(self):
        self.__conn = config.conn
    #数据库查询操作
    def selectMySQL(self,index1,index2):
        rows = []
        try:
            conn = pymysql.connect(**self.__conn)
            cur = conn.cursor()
        except Exception as e:
            print('数据库连接失败:',e)
        else:
            cur.execute('SELECT * FROM element')
            data = cur.fetchall()
            for d in data:
                rows.append(d)
            # print(rows[index1][index2])
            return rows[index1][index2]
        finally:
            cur.close()
            conn.close()
    def get_One(self,sql,params):
        try:
            conn = pymysql.connect(**self.__conn)
            cur = conn.cursor()
            cur.execute(sql, params)
            data = cur.fetchall()
            return  data
        except Exception as e:
            print('数据库连接失败:',e)
        finally:
            cur.close()
            conn.close()
    #数据库插入操作
    def insertMySQL(self,sql,params):
        try:
            conn = pymysql.connect(**self.__conn)
            cur = conn.cursor()
            cur.execute(sql,params)
            conn.commit()
        except Exception as e:
            print('操作mysql数据库失败',e)
        else:
            print('插入后表的数据为:',self.selectMySQL)
        finally:
            cur.close()
            conn.close()
    #数据库修改操作
    @property
    def updateMySQL(self,sql,params):
        try:
            conn = pymysql.connect(**self.__conn)
            cur = conn.cursor()
            cur.execute(sql, params)
            conn.commit()
        except Exception as e:
            print('操作mysql数据库失败',e)
        else:
            print('修改后表的数据为:',self.selectMySQL)
        finally:
            cur.close()
            conn.close()
    #数据库删除操作
    @property
    def deleteMySQL(self,sql,params):
        try:
            conn = pymysql.connect(**self.__conn)
            cur = conn.cursor()
            cur.execute(sql, params)
            conn.commit()
        except Exception as e:
            print('操作mysql数据库失败',e)
        else:
            print('删除后表的数据为:',self.selectMySQL)
        finally:
            cur.close()
            conn.close()
class SqliteHelper(object):
    def selectSqlite(self,value1,value2):
        rows=[]
        try:
            conn=sqlite3.connect(Config.data_dirs()+'/mydatabase.db')
            cur=conn.cursor()
            sql="select *  from element"
            cur.execute(sql)
            data=cur.fetchall()
            for d in data:
                rows.append(d)
            return rows[value1][value2]
        except Exception as e:
            print('操作sqlite3数据库失败',e)
        finally:
            cur.close()
            conn.close()

class User(object):
    def __init__(self):
        self.__helper = MySQLHelper()
    def get_One(self,id):
        sql = 'select * from account where id = %s'
        params = (id,)
        return self.__helper.get_One(sql,params)
    def checkValidate(self,name,address):
        sql = 'select * from account where username = %s and address = %s'
        params = (name,address,)
        return self.__helper.get_One(sql,params)