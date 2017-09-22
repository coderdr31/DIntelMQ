#!/usr/bin/python3
# coding: utf-8

import xlwt
import json

'''
path = "1.xls"
wb=xlwt.Workbook()
sheet=wb.add_sheet("xlwt数据测试表")
value = [["名称", "hadoop编程实战", "hbase编程实战", "lucene编程实战"], ["价格", "52.3", "45", "36"], ["出版社", "机械工业出版社", "人民邮电出版社", "华夏人民出版社"], ["中文版式", "中", "英", "英"]]
for i in range(0,4):
    for j in range(0,len(value[i])):
        sheet.write(i,j,value[i][j])
wb.save(path)
print("写入数据成功！")
'''
# 将intelmq的field各个值写入xls

path1 = "field.xls"
wb = xlwt.Workbook()
sheet1 = wb.add_sheet("sheet1")
headlist = ["name", "description", "type", "length", "regex", "iregex"]
for i in range(0, len(headlist)):
    sheet1.write(0, i, headlist[i])

filepath = "/opt/intelmq/etc/harmonization.conf"
with open(filepath,'r') as f1:
    config = json.loads(f1.read())
    config = config['event']
    i = 1
    for key1, value1 in config.items():
        sheet1.write(i, 0, key1)
        for key2, value2 in value1.items():
            sheet1.write(i, headlist.index(key2),value2)
        i = i+1
    wb.save(path1)
print("写入数据成功")










