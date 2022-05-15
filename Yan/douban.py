# -*- codeing= utf-8 -*-
# @Time : 2022/5/15 11:12
# @Author : Yina
# @File : f.py
# @Software: PyCharm

from bs4 import BeautifulSoup #网页解析
import re   #正则表达式，进行文字匹配
import urllib.request,urllib.error  #制定URL
import xlwt     #进行Excel操作
import sqlite3  #进行SQLite数据库操作

def main():
    baseurl="https://movie.douban.com/top250?start="
    # 1、爬取网页
    datalist=getData(baseurl)
    savepath=".\\豆瓣电影Top250.xls"
    # 3、保存数据
    saveData(savepath)

def getData(baseurl):
    datalist=[]
    # 2、逐一解析数据
    return datalist

# 保存数据
def saveData(savepath):
    print(" ")

if __name__=='__main__':
    main()
