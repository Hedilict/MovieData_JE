# -*-coding:utf8 -*-
# author:Hedilict
import time
import pymysql
from user.MD5 import md5
from user.get_net_time import get_webservertime
from user.key_parameter import *


class movie(object):
    def __init__(self, movie_name, movie_type, start_time, end_time, position, keywords):
        self.__position = position
        self.__movie_name = movie_name
        self.__movie_type = movie_type
        self.__start_time = start_time
        self.__end_time = end_time
        self.__keywords = keywords

    # 获取电影名称、类型（3D和非3D）、开始上映时间、结束放映时间、开放时间、座位位置的方法
    @property
    def name(self):
        return self.__movie_name

    @property
    def type(self):
        return self.__movie_type

    @property
    def start_time(self):
        return self.__start_time

    @property
    def end_time(self):
        return self.__end_time

    @property
    def open_time(self):
        start_dtime = time.strptime(self.start_time, '%Y-%m-%d %H:%M:%S')
        start_stime = time.mktime(start_dtime)
        open_stime = start_stime - time_advance
        open_dtime = time.localtime(open_stime)
        __open_time = time.strftime('%Y-%m-%d %H:%M:%S', open_dtime)
        return __open_time

    @property
    def position(self):
        return self.__position

    @property
    def keywords(self):
        return self.__keywords

    @property
    def MD5(self):
        return md5(self.__keywords)

    # 设置电影名称、类型（3D和非3D）、开始上映时间、结束放映时间、开放时间、座位位置的方法
    @name.setter
    def name(self, value):
        self.__movie_name = value

    @type.setter
    def type(self, value):
        self.__movie_type = value

    @start_time.setter
    def start_time(self, value):
        self.__start_time = value

    @end_time.setter
    def end_time(self, value):
        self.__end_time = value

    @position.setter
    def position(self, value):
        self.__position = value


# 向数据库插入数据
# 参数：名称、类型（int(是否3D)）、开始时间、结束时间、关键词（varchar(180)）、MD5加密
# 关于电影表明的建立还需要具体信息的进一步确定
# 更新：可以实现一次性的插入，批量插入还需调试
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
            "Insert Into " + 'movie_1' + "(movie_name,movie_type,start_time,end_time,position,keywords,MD5) VALUES(%s,%s,%s,%s,%s,%s,%s);",
            (arg[0], int(arg[1]), arg[2], arg[3], arg[4], arg[5], arg[6]))
    else:
        cur.execute("Insert into movie_index(movie_id,movie_name,open_time) values(%s,%s,%s)",
                    (row[0] + 1, arg[0], arg[7]))
        cur.execute("create table " + 'movie_' + str(row[
                                                         0] + 1) + "(movie_name varchar(30) not null,movie_type int(1) not null ,start_time varchar(30) not null,end_time varchar(30) not null,position varchar(30) not null, keywords varchar(185) not null,MD5 varchar(32) not null )engine=innodb default charset=utf8;")

        # 插入str
        cur.execute("Insert Into " + 'movie_' + str(int(row[
                                                            0]) + 1) + "(movie_name,movie_type,start_time,end_time,position,keywords,MD5) VALUES(%s,%s,%s,%s,%s,% s,%s);",
                    (arg[0], int(arg[1]), arg[2], arg[3], arg[4], arg[5], arg[6]))

    # 关闭
    cur.close()
    conn.commit()
    conn.close()


# 检索数据库（通过关键词）
# 基本功能实现(还需添加小于电影结束时间的判断)
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

# 检测远程数据库更新状态
def IsDataUpdate():
    pass


# 检测是否底层有数据传入
def IsDataInput():
    pass
