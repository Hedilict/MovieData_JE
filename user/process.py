# -*-coding=utf8 -*-
# author:Hedilict
import time
from user.data_method import IsDataUpdate, data_insert, IsDataInput, data_search
from user.key_parameter import *


# 数据插入过程
def data_insert_process():
    insert_success = 0
    l = [1,2,3,4,5,6]
    if IsDataUpdate == 0:
        print("未检测到数据更新.")
        time.sleep(success_DataSearch_interval)
        return 0
    else:
        if data_insert(l) == 1:
            print("数据插入成功")
            time.sleep(success_DataSearch_interval)
            return 1
        else:
            for i in range(10):
                print("数据插入失败，正在重新尝试")
                insert_success = 0
                while insert_success == 0:
                    insert_success = data_insert(l)
            if insert_success == 1:
                print("插入成功")
                time.sleep(success_DataSearch_interval)
                return 1
            else:
                print("请检查网络连接和数据库状态,重新尝试")
                time.sleep(fail_DataSearch_interval)
                return 0


# 数据检索过程
def data_search_process():
    if IsDataInput == 0:
        print("未查询到该数据")
        time.sleep(1)
        return 0
    else:
        print("查询成功")
        time.sleep(1)
        return data_search()
if __name__ == '__main__':
    data_insert_process()
    data_search_process()