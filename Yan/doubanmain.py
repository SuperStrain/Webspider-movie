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

findLink=re.compile(r'<a href="(.*?)">')      #影片链接
findimg=re.compile(r'<img.*src="(.*?)" width.*>')#影片图片，re.S表示让换行符包含在其中
findtitle=re.compile(r'<span class="title">(.*?)</span>')#片名
findscore=re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')#影片评分
findFilmcritic=re.compile(r'<span>(\d*)人评价</span>')#影评人数
findoverview=re.compile(r'<span class="inq">(.*)</span>')#找到影片概况
findcontent=re.compile(r'<p class="">(.*?)</p>',re.S)#影片内容

def getData(baseurl):
    datalist=[]
    for i in range(0,10):
        url=baseurl+str(i*25)
        #https://movie.douban.com/top250?start=i*25
        html=askULR(url)
        # 2、逐一解析数据
        soup =BeautifulSoup(html,"html.parser")
        for item in soup.find_all('div',class_="item"): #类要加下划线,查找符合要求的字符串形成列表
            # print(item) #测试，查看电影item全部信息
            data=[]     #保存一部电影的所有信息
            item=str(item)
            link=re.findall(findLink,item)[0]#re库铜锅正则表达式查找第一个信息信息
            img=re.findall(findimg,item)[0]
            title=re.findall(findtitle,item)  #片名只有一个中文名
            score=re.findall(findscore,item)[0]
            filmcritic=re.findall(findFilmcritic,item)[0]
            overview=re.findall(findoverview,item)[0]
            content=re.findall(findcontent,item)[0]
            print(content)
    return datalist


#得到指定一个URL网页内容
def askULR(url):
    head={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"}
        #head信息用于伪装成浏览器，User-Agent，告诉豆瓣服务器我们能接受怎样格式的信息
    request=urllib.request.Request(url,headers=head)
    html=""
    try:
        response=urllib.request.urlopen(request)
        html=response.read().decode('utf-8')
        # print(html)
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

