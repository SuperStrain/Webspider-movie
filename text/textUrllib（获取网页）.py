# -*- codeing= utf-8 -*-
# @Time : 2022/5/15 11:12
# @Author : Yina
# @File : f.py
# @Software: PyCharm
import urllib.request
#1、获取一个get请求
# response=urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode('utf-8'))#对获取到的网页进行utf-8解码（防止中文乱码）

#2、使用httpbin.org进行如下请求（主要是post请求借助该网站）

#（1）get请求,并为超时做一个计划性的异常处理
# try:
#     response=urllib.request.urlopen("http://httpbin.org/get",timeout=0.01)
#     print(response.read().decode('utf-8'))
# except urllib.error.URLError as e:
#     print(e)
#     print("超出预计时间!!")

# （2）获取一个post请求:用于模拟用户真实登录时使用(注意：http://httpbin.org可用于测试)
# import urllib.parse #解析
# data=bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8") # 提交一个表单信息才能访问（可以是用户名、密码、cookie等）
# response=urllib.request.urlopen("http://httpbin.org/post",data=data)
# print(response.read().decode('utf-8'))


# response=urllib.request.urlopen("http://www.baidu.com")
# # print(response.status)
# print(response.getheaders())

#豆瓣拒绝爬虫访问，设置伪装成浏览器访问
# （1）httpbin测试
# url="http://httpbin.org/post"
# headers={"User-Agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"}
# data=bytes(urllib.parse.urlencode({"name":"Yina"}),encoding="utf-8")
# req=urllib.request.Request(url=url,data=data,headers=headers,method="POST")
# response=urllib.request.urlopen(req)
# print(response.read().decode('utf-8'))

#（2）豆瓣访问
url="https://www.douban.com/"
headers={"User-Agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"}
req=urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(req)
print(response.read().decode('utf-8'))
