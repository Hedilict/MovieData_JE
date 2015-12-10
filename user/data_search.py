# -*- coding:utf8 -*-
# author: Hedilict

import pymysql


from user.MD5 import md5
from user.key_parameter import *
from user.get_net_time import get_webservertime


def data_search(value):
    # 连接数据库
    conn = pymysql.Connect(host=host, user=user, passwd=password, charset=charset)

    # 游标
    cur = conn.cursor()

    # 找到数据库
    cur.execute("USE je_tech_movie")

    # 确定当前网络时间
    nowtime = get_webservertime("www.baidu.com")

    # 首先检索电影开放时间对应表
    cur.execute("select movie_id,open_time from movie_index")
    rows = cur.fetchall()
    for row in rows:
        if nowtime > row[1]:
            cur.execute("select MD5 from %s where MD5 = %r" % ("movie_"+str(row[0]), value))
            res = cur.fetchall()
            if len(res) == 0:
                print("未找到这张电影票")
                return 0
            else:
                print("找到电影票，允许进入")
                return 1
    print("还未到检票时间哦")
    return -1

    # 关闭
    cur.close()
    conn.commit()
    conn.close()


if __name__ == '__main__':
    value = input("请输入要查找的数据:")
    isFind = data_search(md5(str(value)))
    print(isFind)
