#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
#创建文件夹目录
# os.mkdir("potato")
##当前目录下面的文件列表
print(os.listdir("../"))
# os.removedirs("potato")
#获取当前路径(目录)
print(os.getcwd())
# print(os.path.abspath("__filename__"))
if not os.path.exists("../b"):
    os.mkdir("../b")
# if not os.path.exists("b"):
#     f=open("b","w")


import datetime
import  time
##西方时间
print(time.asctime())
#时间戳
print(time.time())
#当前时间，元组
print(time.localtime())
##转换成格式化时间
print(time.strftime("%Y年%m月%d日 %H:%M:%S", time.localtime()))
#两天前的时间
nowtime=time.time()
twodaytime=nowtime-3600*24*2
time_tupe=time.localtime(twodaytime)
print(time.strftime("%Y年%m月%d日 %H:%M:%S", time_tupe))
#网络请求
import urllib.request
response=urllib.request.urlopen("http://www.baidu.com")
print(response.status)

##计算
import math

print(math.ceil(5.5))

