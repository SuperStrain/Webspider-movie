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
html=file.read()
bs=BeautifulSoup(html,"html.parser")

#1、-Tag 标签及其内容：拿到他所找到的第一个内容
print(bs.title)
print(type(bs.title))
#2、-NavigableString
print(bs.title)
print(type(bs.title))