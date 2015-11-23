# -*- coding:utf8 -*-
# author: Hedilict

import pymysql


def data_search(value):
    # 连接数据库
    conn = pymysql.Connect(host='127.0.0.1', user='root', passwd='zjn950101')

    # 游标
    cur = conn.cursor()

    # 找到数据库
    cur.execute("USE je_tech")

    # 查询
    cur.execute("Select keywords from movie_data")
    for row in cur.fetchall():
        if (row[0] == value):
            return 1
        else:
            continue
        return 0

    # 关闭
    cur.close()
    conn.commit()
    conn.close()


if __name__ == '__main__':
    value = input("请输入要查找的数据:")
    isFind = data_search(str(value))
    if isFind:
        print("找到这条数据！")
    else:
        print("未找到这条数据！")
