#!/usr/bin/env python
#coding=utf-8
###################################
# @author migle
# @date 2010-01-17
##################################
#MySQLdb 示例
#
##################################
import MySQLdb

#建立和数据库系统的连接
conn = MySQLdb.connect(host='localhost', user='root',passwd='')

#获取操作游标
cursor = conn.cursor()
#执行SQL,创建一个数据库.
cursor.execute("""create database if not exists python""")

#选择数据库
conn.select_db('python');
#执行SQL,创建一个数据表.
cursor.execute("""create table test(id int, info varchar(100)) """)

value = [1,"inserted ?"];

#插入一条记录
cursor.execute("insert into test values(%s,%s)",value);

values=[]


#生成插入参数值
for i in range(20):
    values.append((i,'Hello mysqldb, I am recoder ' + str(i)))
#插入多条记录

cursor.executemany("""insert into test values(%s,%s) """,values);

#关闭连接，释放资源
cursor.close();