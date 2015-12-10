# -*-coding:utf8 -*-
# author: Hedilict
"""
多进程实现数据的获取、插入数据库、以及影票检索的过程
"""

import user.data_method
import os
import random
import time
from multiprocessing import Pool

from user.process import data_search_process, data_insert_process

search_state = 0
data_update_state = 0
while True:
    p = Pool()
    p.apply_async(data_insert_process(), args=())
    if search_state == 1:
        data_search_process()

