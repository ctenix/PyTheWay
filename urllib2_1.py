#First add the # -*- coding: utf-8 -*- line to the beginning of the file
#use u'foo' for all your non-ASCII unicode data
#coding: utf8 
import urllib2
#直接获取内容
response = urllib2.urlopen('http://www.baidu.com')
#获取返回码，200表示获取成功
print response.getcode()

#读取内容
cont = response.read()
print cont