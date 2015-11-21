# -*- coding:utf-8 -*-
#author: Hedilict

import pymysql

#连接数据库
conn=pymysql.Connect(host='127.0.0.1', user='root', passwd='zjn950101')
#游标
cur=conn.cursor()

try:
    cur.execute("Drop database foo")
except Exception as e:
    print(e)
finally:
    pass

#创建数据库
cur.execute("CREATE DATABASE foo")
cur.execute("USE foo")

#创建表
cur.execute("Create Table users(id INT,name varchar(20))")
#插入

cur.execute("Insert Into users VALUES(1,'yuanben'),(2,'zhangjianing'),(3,'huahanxin')")
#查询
cur.execute("Select * from users")
for row in cur.fetchall():
    print("%s\t%s"
          %row)


#关闭
cur.close()
conn.commit()
conn.close()
