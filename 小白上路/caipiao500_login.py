#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/6/28 17:54
# @Author  : 伯明
# @Site    : 
# @File    : caipiao500_login.py
# @Software: PyCharm
import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# http://wwww-caipiao500.com/login 某彩票网站, 需具体确定加密逻辑

import hashlib
import random
import base64


def s(t):
    return hashlib.md5(t.encode(encoding="utf-8")).hexdigest()


def base64_encrypt(t):
    return bytes.decode(base64.b64encode(t.encode("utf-8")))


def c(u, p):
    """账号, 密码"""
    return s(u.lower() + s(p))


def login_data(e):
    """
    传入登录的信息 (账号、密码)
    :param e:
    :return:
    """
    t = "dafacloud_" + str(random.random())
    e["random"] = base64_encrypt(t)
    i = c(e["userName"], e["password"])
    e["password"] = s(i + t)  # 最终密码是账号名小写+密码md5组合，进一步md5生成i, i+t生产最终密码
    return e


if __name__ == '__main__':
    login_info = {"userName": "AA123456", "password": "123456"}
    print(login_data(login_info))
