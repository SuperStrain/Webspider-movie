# -*- codeing= utf-8 -*-
# @Time : 2022/5/15 11:12
# @Author : Yina
# @File : f.py
# @Software: PyCharm
import urllib.request
#获取一个get请求
# response=urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode('utf-8'))#对获取到的网页进行utf-8解码（防止中文乱码）

#使用httpbin.org进行如下请求（主要是post请求借助该网站）

#get请求,并为超时做一个计划性的异常处理
# try:
#     response=urllib.request.urlopen("http://httpbin.org/get",timeout=0.01)
#     print(response.read().decode('utf-8'))
# except urllib.error.URLError as e:
#     print(e)
#     print("超出预计时间!!")

# 获取一个post请求:用于模拟用户真实登录时使用
import urllib.parse #解析
data=bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8") # 提交一个表单信息才能访问（可以是用户名、密码、cookie等）
response=urllib.request.urlopen("http://httpbin.org/post",data=data)
print(response.read().decode('utf-8'))


# response=urllib.request.urlopen("http://www.baidu.com")
# # print(response.status)
# print(response.getheaders())
