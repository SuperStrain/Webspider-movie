# -*- codeing= utf-8 -*-
# @Time : 2022/5/15 11:12
# @Author : Yina
# @File : f.py
# @Software: PyCharm

# 正则表达式即是字符串模式（判断字符串是否符合一定标准）

import re
# 1、search
# pat=re.compile("AA")#此处AA为正则表达式，用于验证其他字符
#搜索字符串被校验的内容，search方法用于查找比对
# m=pat.search("CBA") #不符合要求的
# m=pat.search("ABCAA")#符合要求的第一个内容

# m=re.search("asd","Aasdgg")#前面的为规则，后面的为查找对象（内容）
# print(m)

#2、findall
# m=re.findall("a","AaAadfgAa")#前面是规则，后面是查找内容，找到所有
# print(m)
# print(re.findall("[A-Z]","gKJhYkjHhik"))#找到所有大写字母，运用了正则表达式
# print(re.findall("[A-Z]+","gKJhYkjHhik"))#找到至少一个以上的连续大写字母

#3、sub 替换功能
# print(re.sub("a","A",r"\a\bcdasd"))#找到a用A替换，最后的是查找内容
# #建议在被比较的字符前面加上r防止转义字符生效

