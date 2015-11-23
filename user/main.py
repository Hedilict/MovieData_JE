# -*-coding:utf8 -*-
# author: Hedilict

from data_search import *
from data_insert import *


class movie(object):
    def __init__(self, id, name, type, start_time, end_time, open_time, position):
        self.__position = position
        self.__open_time = open_time
        self.__name = name
        self.__type = type
        self.__start_time = start_time
        self.__end_time = end_time

    # 获取电影名称、类型（3D和非3D）、开始上映时间、结束放映时间、开放时间、座位位置的方法
    @property
    def name(self):
        return self.__name

    @property
    def type(self):
        return self.__type

    @property
    def start_time(self):
        return self.__start_time

    @property
    def end_time(self):
        return self.__end_time

    @property
    def open_time(self):
        return self.__open_time

    @property
    def position(self):
        return self.__position

    # 设置电影名称、类型（3D和非3D）、开始上映时间、结束放映时间、开放时间、座位位置的方法
    @name.setter
    def name(self, value):
        self.__name = value

    @type.setter
    def type(self, value):
        self.__type = value

    @start_time.setter
    def start_time(self, value):
        self.__start_time = value

    @end_time.setter
    def end_time(self, value):
        self.__end_time = value

    @open_time.setter
    def open_time(self,value):
        self.__open_time = value

    @position.setter
    def position(self,value):
        self.__position = value



data_insert()
data_search()
