# -*-coding:utf8 -*-
# author:Hedilict
'''
关于电影表明的建立还需要具体信息的进一步确定
'''

import pymysql

from user.MD5 import md5
from user.key_parameter import *


def data_insert(arg):
    # 连接数据库
    conn = pymysql.Connect(host=host, user=user, passwd=password, charset=charset)

    # 游标
    cur = conn.cursor()

    # 找到数据库
    cur.execute("USE je_tech_movie")

    # 在检索电影表中找到最大的ID
    cur.execute("Select max(movie_id) from movie_index")
    row = cur.fetchone()
    print(row[0])


    # 关闭
    cur.close()
    conn.commit()
    conn.close()


if __name__ == '__main__':
    message = ['sdd',1,'sads','asfgg','sdfdf','sdggthth']
    message.append(md5(message[5]))
    data_insert(message)
    print("插入成功！")
