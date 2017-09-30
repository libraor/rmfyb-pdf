#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from datetime import datetime
from catch import catch_pdf  #从catch.py 中调取catch_pdf()函数
from mail import mail_pdf #从mail.py中调取mail_pdf()函数

#start

print "抓取程序开始运行..."
now = datetime.now() # 获取当前时间
baseday = datetime.strptime('2010-12-30', '%Y-%m-%d') #周四基准日
print "当前时间为:"
print (now)

if (now - baseday).days %7 != 0: #判断是否为周四，如果是则执行下一步
    print('今天是周四，抓取开始')
    file06,file07 = catch_pdf() #抓取文件，并返回生成的文件名
    print "已从服务器抓取 "+file06,file07
    ret = mail_pdf(file06,file07) #将文件名传递到mail_pdf()函数中，并发送邮件
    if ret:
        print("邮件发送成功")
    else:
        print("邮件发送失败")
else:
    print("今天不是周四，程序终止")
