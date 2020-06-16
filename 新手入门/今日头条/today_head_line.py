#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/6/16 9:50
# @Author  : 伯明
# @Site    : 
# @File    : today_head_line.py
# @Software: PyCharm
import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# py版本的as、cp参数解密, 网上的

import math
import time
import hashlib


def get_as_cp():
    e = math.floor(int(str(time.time() * 1000).split('.')[0]) / 1e3)  # 获取13位毫秒数然后除于1e3再向下取整
    i = str('%X' % e)  # 转换e为16进制
    m5 = hashlib.md5()
    m5.update(str(e).encode('utf-8'))
    t = str(m5.hexdigest()).upper()  # 进行md5加密
    if 8 != len(i):
        return {'as': '479BB4B7254C150', 'cp': '7E0AC8874BB0985'}
    o = t[0:5]
    n = t[-5:]
    a = ""
    r = ""
    for x in range(5):  # 交换字符串
        a += o[x] + i[x]
        r += i[x + 3] + n[x]
    return {'as': "A1" + a + i[-3:], 'cp': i[0:3] + r + "E1"}


if __name__ == '__main__':
    print(get_as_cp())
