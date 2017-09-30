#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
from email.header import Header
from pw import pw
from content import content_title_link


def mail_pdf(file06,file07): #参数传入附件的文件名
    ret = True
    my_sender,my_pass,my_user = pw() #传入发件邮箱、密码、收件邮箱
    try:
        print("开始生成邮件")
        #print file06,file07
        msg=MIMEMultipart()
        #邮件正文内容
        msg.attach(MIMEText('邮件发送测试……/n不要看我...看疗效...', 'plain', 'utf-8'))
        msg['From']=formataddr(["Leon",my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] =  Header("VIP", 'utf-8')  #括号中填写收件人昵称
        msg['Subject']="邮件测试"                # 邮件的主题，也可以说是标题
        #构造附件1，传送当前目录下的 file06.pdf 文件
        att1 = MIMEText(open(file06, 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        att1.add_header('Content-Disposition', 'attachment',filename = file06) #filename为附件名
        msg.attach(att1)
        # 构造附件2，传送当前目录下的 file07.pdf 文件
        att2 = MIMEText(open(file07, 'rb').read(), 'base64', 'utf-8')
        att2["Content-Type"] = 'application/octet-stream'
        print file06,file07
        att2.add_header('Content-Disposition', 'attachment',filename = file07)
        msg.attach(att2)
        #发件
        print("开始发送邮件")
        server=smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人QQ邮箱中的SMTP服务器，端口是465
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender,my_user,msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret=False
    return ret #返回是否成功

def mail_title_link():
    #将标题和链接列表ctl，转化为字符串text，以用于邮件发送
    ctl = content_title_link()
    text = ''
    n=0
    while n < len(ctl):
        text += str(ctl[n]) +'\n'
        n += 1
    
    ret=True
    my_sender,my_pass,my_user = pw() #传入发件邮箱、密码、收件邮箱
    try:
    
        print("开始生成邮件")
        msg=MIMEMultipart()
        #邮件正文内容
        msg.attach(MIMEText(text, 'plain', 'utf-8'))
        msg['From']=formataddr(["Leon",my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] =  Header("VIP", 'utf-8')  #括号中填写收件人昵称
        msg['Subject']="邮件测试"                # 邮件的主题，也可以说是标题
        #发件
        print("开始发送邮件")
        server=smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender,my_user,msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret=False
    return ret #返回是否成功