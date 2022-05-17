# -*- codeing= utf-8 -*-
# @Time : 2022/5/15 11:12
# @Author : Yina
# @File : f.py
# @Software: PyCharm

import xlwt

#创建对象
#创建工作表
#写入数据，第一个参数“行”，第二个参数“列”，第三个参数内容
#保存数据表

workbook=xlwt.Workbook(encoding='utf-8')
worksheet=workbook.add_sheet('sheet1')
#打印九九乘法表
# for i in range(9):
#     for j in range(i+1):
#         worksheet.write(i,j,'%d*%d=%d'%(i+1,j+1,(i+1)*(j+1)))
worksheet.write(0,0,"Hello Student")
workbook.save('student.xls')