# -*- codeing= utf-8 -*-
# @Time : 2022/5/15 11:12
# @Author : Yina
# @File : f.py
# @Software: PyCharm

# BeautifulSoup4将一个复杂的HTML文档转换成一个复杂的树形结构，每个节点都是Python对象，所有对象可以归纳为4种：
# 1、-Tag
# 2、-NavigableString
# 3、-BeautifulSoup
# 4、-Comment
from bs4 import BeautifulSoup
file=open("./百度.html","rb")
html=file.read().decode('utf-8')
bs=BeautifulSoup(html,"html.parser")

#1、-Tag 标签及其内容：拿到他所找到的第一个内容
# print(bs.title)
# print(type(bs.title))

#2、-NavigableString 标签里的内容（字符串）
# print(bs.title.string)
# print(type(bs.title.string))

#3、-BeautifulSoup 表示整个文档
# print(bs)
# print(type(bs))

#4、-Comment 特殊的NavigableString ，输出的内容不包含注释符

#应用：
#文档的遍历
# print(bs.head.contents)


#文档的搜索(主要)

#（1）find_all() 字符串过滤，查找与字符串完全相同的内容
# t_list=bs.find_all("a") #带<a>的
# for item in t_list:
#     print(item)

#正则表达式搜索 使用search()的方法来查找内容,只要有元素'a'即可
import re
# t_list=bs.find_all(re.compile("a"))
# for item in t_list:
#     print(item)

#传入有个函数（方法），根据函数的方法来搜索
# def name_is_exists(tag):
#     return tag.has_attr("name")
#
# t_list=bs.find_all(name_is_exists)
# for item in t_list:
#     print(item)

#（2）kwargs    参数
# t_list=bs.find_all(id="head")
# t_list=bs.find_all(href="http://news.baidu.com")
# for item in t_list:
#     print(item)

# (3)text  参数
# t_list=bs.find_all(text=["hao123","地图"])
# t_list=bs.find_all(text=re.compile("\d"))#应用正则表达式来查找包含特定文本的内容（标签里的字符串）
# for item in t_list:
#     print(item)

#（4）limit 参数 限制搜索数量
# t_list=bs.find_all("a")
# t_list=bs.find_all("a",limit=3)
# for item in t_list:
#     print(item)


#选择器 css
# t_list=bs.select('title')  #通过标签来查找
# t_list=bs.select(".mnav") #通过类名来查找
# t_list=bs.select("#u1") #通过id来查找
# t_list=bs.select("a[class='bri']")#通过属性来查找
# t_list=bs.select("head > title")#通过子标签来查找
# for item in t_list:
#     print(item)

# t_list=bs.select(".mnav ~ .bri")#查找在mnav类别里的bri类别
# print(t_list[0].get_text())#获取第一个元素文本