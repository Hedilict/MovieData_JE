# -*-coding:utf8 -*-
# author:Hedilict
'''
关于电影表明的建立还需要具体信息的进一步确定
'''

import pymysql
from user.MD5 import md5
from user.data_method import movie
from user.key_parameter import *


def data_insert(arg):
    # 连接数据库
    conn = pymysql.Connect(host=host, user=user, passwd=password, charset=charset)

    # 游标
    cur = conn.cursor()

    # 找到数据库
    cur.execute("USE je_tech_movie")

    # 在检索电影表中找到最大的ID
    cur.execute("Select max(movie_id) from  movie_index")
    row = cur.fetchone()
    if isinstance(row[0], type(None)):
        # 创建检索电影表的对应的数据
        cur.execute("Insert into movie_index(movie_id,movie_name,open_time) values(1,%s,%s)", (arg[0], arg[7]))

        # 创建相应的电影的表
        cur.execute(
            "create table " + 'movie_1' + "(movie_name varchar(30) not null,movie_type int(1) not null ,start_time varchar(30) not null,end_time varchar(30) not null,position varchar(30) not null, keywords varchar(185) not null,MD5 varchar(32) not null )engine=innodb default charset=utf8;")

        # 插入str
        cur.execute(
            "Insert Into " + 'movie_1' + "(movie_name,movie_type,start_time,end_time,position,keywords,MD5) VALUES(%s,%s,%s,%s,%s,%s,%s);",(arg[0], int(arg[1]), arg[2], arg[3], arg[4], arg[5], arg[6]))
    else:
        cur.execute("Insert into movie_index(movie_id,movie_name,open_time) values(%s,%s,%s)", (row[0] + 1, arg[0], arg[7]))
        cur.execute("create table " + 'movie_' + str(row[0] + 1) + "(movie_name varchar(30) not null,movie_type int(1) not null ,start_time varchar(30) not null,end_time varchar(30) not null,position varchar(30) not null, keywords varchar(185) not null,MD5 varchar(32) not null )engine=innodb default charset=utf8;")

        # 插入str
        cur.execute("Insert Into " + 'movie_' + str(int(row[0]) + 1) + "(movie_name,movie_type,start_time,end_time,position,keywords,MD5) VALUES(%s,%s,%s,%s,%s,% s,%s);", (arg[0], int(arg[1]), arg[2], arg[3], arg[4], arg[5], arg[6]))

    # 关闭
    cur.close()
    conn.commit()
    conn.close()


if __name__ == '__main__':
    message = []
    for i in range(6):
        value = input("请输入数据:")
        message.append(value)
    message.append(md5(message[5]))
    Movie = movie(message[0], message[1], message[2], message[3], message[4], message[5])
    temp = Movie.open_time
    message.append(temp)
    data_insert(message)
    print("插入成功！")
