#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from datetime import datetime
import urllib
from urllib.request import urlretrieve


def catch_pdf():
    now = datetime.now() # 获取当前时间
    #分解now，并生成PDF链接
    Ym = now.strftime('/%Y-%m/')
    d = now.strftime('%d/')
    Ymd = now.strftime('%Y%m%d')
    Ymd06 = now.strftime('%Y%m%d''06_pdf.pdf')
    Link06 = 'http://rmfyb.chinacourt.org/paper/images' + Ym + d + '06/' +Ymd06 #第六版链接
    Ymd07 = now.strftime('%Y%m%d''07_pdf.pdf')
    Link07 = 'http://rmfyb.chinacourt.org/paper/images' + Ym + d + '07/' +Ymd07 #第七版链接
    #print Link06,Link07
    #保存本地
    urlretrieve(Link06, Ymd + '06.pdf')
    urlretrieve(Link07,Ymd + '07.pdf')
    return Ymd+'06.pdf',Ymd+'07.pdf' #返回生成的文件名

def catch_contentlink():
    now = datetime.now() # 获取当前时间
    #分解now，并生成版面网页链接
    Ym = now.strftime('/%Y-%m/')
    d = now.strftime('%d/')
    #Ymd = now.strftime('%Y%m%d')
    Link_f = 'http://rmfyb.chinacourt.org/paper/html' + Ym + d + 'content_' #传至content.py中，用于获取文章页
    Ymd06 = now.strftime('node_7.htm')
    Link06 = 'http://rmfyb.chinacourt.org/paper/html' + Ym + d + Ymd06 #第六版网页链接
    Ymd07 = now.strftime('node_8.htm')
    Link07 = 'http://rmfyb.chinacourt.org/paper/html' + Ym + d + Ymd07 #第七版网页链接
    print (Link_f,Link06,Link07)
    #保存本地
    return Link_f,Link06,Link07 #返回生成的文件名
