#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 14:28:35 2017

@author: Leon
"""

from datetime import datetime
import urllib
import os
os.system("mail.py")

def catch():
     #分解now，并生成PDF链接
    Ym = now.strftime('/%Y-%m/')
    d = now.strftime('%d/')
    Ymd = now.strftime('%Y%m%d')
    Ymd06 = now.strftime('%Y%m%d''06_pdf.pdf')
    Link06 = 'http://rmfyb.chinacourt.org/paper/images' + Ym + d + '06/' +Ymd06 #第六版链接
    Ymd07 = now.strftime('%Y%m%d''07_pdf.pdf')
    Link07 = 'http://rmfyb.chinacourt.org/paper/images' + Ym + d + '07/' +Ymd07 #第七版链接
    print Link06,Link07
    #保存本地
    urllib.urlretrieve(Link06, Ymd + '06.pdf')
    urllib.urlretrieve(Link07,Ymd + '07.pdf')
    return Ymd+'06.pdf',Ymd+'07.pdf' #返回生成的文件名

print "抓取程序开始运行..."
now = datetime.now() # 获取当前时间
baseday = datetime.strptime('2010-12-30', '%Y-%m-%d') #周四基准日


if (now - baseday).days %7 != 0: #判断是否为周四，如果是则执行下一步
    print('今天是周四，抓取开始') 
    name06,name07 = catch() #返回生成文件的文件名
    print name06,name07

    ret=mail() #函数在mail.py中
    if ret:
        print("邮件发送成功")
    else:
        print("邮件发送失败")
