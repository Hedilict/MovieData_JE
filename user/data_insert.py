# -*-coding:utf8 -*-
# author:Hedilict

import pymysql


def data_insert(arg):
    # 连接数据库
    conn = pymysql.Connect(host='127.0.0.1', user='root', passwd='zjn950101', charset="utf8")

    # 游标
    cur = conn.cursor()

    # 找到数据库
    cur.execute("USE je_tech")

    # 获取最大id值
    cur.execute("select max(id) from movie_data")
    max_id = cur.fetchall()[0]

    # 插入str
    if max_id[0] is None:   #数据库中没有数据，返回None
        cur.execute("Insert Into movie_data VALUES(%s,%s,%s,%s,%s,%s)",
                (1, arg[0], arg[1], arg[2], arg[3], arg[4]))
    else:
        cur.execute("Insert Into movie_data VALUES(%s,%s,%s,%s,%s,%s)",
                (max_id[0] + 1, arg[0], arg[1], arg[2], arg[3], arg[4]))

    # 关闭
    cur.close()
    conn.commit()
    conn.close()


if __name__ == '__main__':
    message = []
    for i in range(5):
        value = input("请输入数据:")
        message.append((value))
    data_insert(message)
    print("插入成功！")
