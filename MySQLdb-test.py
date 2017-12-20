# -*- coding:utf-8 -*-
import MySQLdb as mysql

# 打开数据库连接
# phthon程序文件名名字和内置模块名字不要重复，重复时会出现方法报错问题
conn = mysql.connect(host ="127.0.0.1", user="subx", passwd="subx1718", db="world")

# 使用cursor()方法获取操作游标
cursor = conn.cursor()
# 使用excute方法执行SQL语句
cursor.execute("SELECT VERSION()")
# 使用fethone（）方法获取一条数据
data = cursor.fetchone()
print "Database version: %s" % data
# 关闭数据库连接
conn.close()
