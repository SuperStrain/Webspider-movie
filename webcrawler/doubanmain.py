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
    datalist=getData(baseurl)   # 1、爬取网页+2、逐一解析数据
    # 3、保存数据
    #（1）保存到Excel表格
    # savepath="豆瓣电影Top250.xls"
    # saveData(savepath, datalist)
    #（2）保存到数据库
    dbpath="movie.db"
    saveDataToDB(dbpath,datalist)


findLink=re.compile(r'<a href="(.*?)">')      #影片链接
findimg=re.compile(r'<img.*src="(.*?)" width.*>')#影片图片，re.S表示让换行符包含在其中
findtitle=re.compile(r'<span class="title">(.*?)</span>')#片名
findscore=re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')#影片评分
findFilmcritic=re.compile(r'<span>(\d*)人评价</span>')#影评人数
findoverview=re.compile(r'<span class="inq">(.*)</span>')#影片概况
findcontent=re.compile(r'<p class="">(.*?)</p>',re.S)#影片内容

#1、爬取网页 +2、逐一解析数据
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

            #添加链接
            link=re.findall(findLink,item)[0]#re库铜锅正则表达式查找第一个信息信息
            data.append(link)

            #添加图片
            img=re.findall(findimg,item)[0]
            data.append(img)

            #添加标题
            title=re.findall(findtitle,item)  #片名只有一个中文名
            if len(title)==2:
                ctitle=title[0]
                data.append(ctitle)
                otitle=title[1].replace("/","")
                otitle=otitle.strip()  #防止出现NBSP乱码！！！！
                data.append(otitle)
            else:
                data.append(title[0])
                data.append(" ")#留空防止Excel表格乱序

            #添加评分
            score=re.findall(findscore,item)[0]
            data.append(score)

            #添加影评
            filmcritic=re.findall(findFilmcritic,item)[0]
            data.append(filmcritic)

            #添加概述（概述有可能不存在）
            overview=re.findall(findoverview,item)  #弄清楚为什么有的可以加[0]，有的不可以？？
            if len(overview)!=0:
                overview=overview[0].replace('。','')
                data.append(overview)
            else:
                data.append(" ")

            #影片内容（主演等）
            content=re.findall(findcontent,item)[0]
            content=re.sub('<br(\s+)?/>(\s+)?'," ",content)#去掉<br/>
            content=re.sub('/'," ",content)  #替换/
            content = content.replace(u'\xa0', ' ')#防止出现NBSP乱码
            content = content.strip()  # 去掉前后的空格
            data.append(content)

            datalist.append(data)   #把处理好的一部电影信息放入到数据列表里
    # print(datalist)  # 用于测试
    return datalist


#得到指定一个URL网页内容
def askULR(url):
    head={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"}
        #head信息用于伪装成浏览器，User-Agent，告诉豆瓣服务器我们能接受怎样格式的信息
    request=urllib.request.Request(url,headers=head)    #向服务器发送请求
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

# 保存数据到Excel表格
def saveData(savepath,datalist):
    workbook = xlwt.Workbook(encoding='utf-8',style_compression=0)
    worksheet = workbook.add_sheet('豆瓣电影top250',cell_overwrite_ok=True)
    #表格头部信息
    col=("电影详情链接","电影图片链接","影片中文名","影片外国名","电影评分","评价人数","电影概况","相关信息")
    for i in range(0,8):
        worksheet.write(0,i,col[i])
    for i in range(0,250):
        print("正在生成第%d条电影资讯"%(i+1))
        data=datalist[i]
        for j in range(0,8):
            worksheet.write(i+1,j,data[j])
    workbook.save(savepath)

#保存到数据库
def saveDataToDB(dbpath,datalist):
    init_db(dbpath)
    conn=sqlite3.connect(dbpath)
    cur = conn.cursor()

    for data in datalist:
        for index in range(len(data)):
            if index==4 or index==5:
                continue
            data[index]='"'+data[index]+'"'
        sql='''
            insert into movie250
            (
            info_link,pic_link,cname,ename,score,rated,instroduction,info
            )
            values(%s)
        '''%",".join(data)
        print(sql)
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()

def init_db(dbpath):
    sql='''
        create table movie250
        (
        id integer primary key autoincrement,
        info_link text,
        pic_link text,
        cname varchar,
        ename varchar,
        score numeric,
        rated numeric,
        instroduction text,
        info text
        )
    '''
    coon = sqlite3.connect(dbpath)
    cursor=coon.cursor()
    cursor.execute(sql)
    coon.commit()
    coon.close()
    print("数据库创建完成！")

if __name__=='__main__':
    main()
    print("爬取完毕！")



