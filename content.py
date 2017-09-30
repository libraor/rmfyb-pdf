#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import re
import urllib2
from catch import catch_contentlink #抓取页面链接


def content_title_link(): #生成文章标题和链接列表
    #获取并生成文章页链接
    for link in Links: #迭代Links，简化代码
        response = urllib2.urlopen(link)
        #print response.read()  只能调用一次，好奇怪，调用第二次就没有了，必须重新“response = urllib2.urlopen(Link06)”获取
        #分析页面，获取版面标题，生成标题列表及链接    
        #正则
        linknum = list(re.findall(r'href=content_(\d*)\.htm\?div',response.read(),re.M)) #跨行匹配，获取文章标题    
        #print linknum 
        #获取文章标题
        response = urllib2.urlopen(link)
        title = re.findall(r'mp\d*>(.*)</div>',response.read(),re.M)   #跨行匹配，获取文章标题  
        #生成链接
        linktocontent =['']*len(linknum) #建立一个长度为linknum列表长度的空列表
        
        i = 0
        ctl = []#将标题和链接依次转入列表
        while i < len(linktocontent): #将标题和链接存入txt文件
            linktocontent[i] = Link_f + linknum[i] + ".htm" #生成完整的文章链接
            #print title[i]
            #print linktocontent[i]
            ctl.extend([title[i],linktocontent[i]])
            ''' 将标题和链接写入TXT文件
            # 打开文件,写入txt文件
            fo = open("test.txt", "a+")
            print "文件名为: ", fo.name
            str1 = title[i] + '\n'
            fo.write( str1 )
            str2 = linktocontent[i] + '\n'
            fo.write( str2 ) 
            # 关闭文件
            fo.close()
            '''
            i += 1
        #for ctl in ctl:
            #print ctl
    return ctl
        
 



#调取页面链接
Link_f,Link06,Link07 = catch_contentlink()
Links = [Link06,Link07]





