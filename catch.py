#!/usr/bin/env python2
# -*- coding: utf-8 -*-


from datetime import datetime
import urllib


def catch():
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
    urllib.urlretrieve(Link06, Ymd + '06.pdf')
    urllib.urlretrieve(Link07,Ymd + '07.pdf')
    return Ymd+'06.pdf',Ymd+'07.pdf' #返回生成的文件名
