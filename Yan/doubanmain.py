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
    askULR("https://movie.douban.com/top250?start=")

def getData(baseurl):
    datalist=[]

    for i in range(0,10):
        url=baseurl+str(i*25)
        html=askULR(url)
        # 2、逐一解析数据
    return datalist


#得到指定一个URL网页内容
def askULR(url):
    head={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"}
        #head信息用于伪装成浏览器，User-Agent，告诉豆瓣服务器我们能接受怎样的信息
    request=urllib.request.Request(url,headers=head)
    html=""
    try:
        response=urllib.request.urlopen(request)
        html=response.read().decode('utf-8')
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html

# 保存数据
def saveData(savepath):
    print(" ")

if __name__=='__main__':
    main()

