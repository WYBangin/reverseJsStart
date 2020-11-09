#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/11/9 17:14
# @Author  : wyb
# @Site    : 
# @File    : common_utils.py
# @Software: PyCharm
import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


def params_to_dict(content):
    """将url中的params参数分割成字典的函数"""
    encrypt_list = [(each.split("=")[0], each.split("=")[-1]) for each in content.split('&')]
    encrypt_dict = dict(encrypt_list)
    return encrypt_dict


def params_join(content):
    """字典转换成字符串的函数"""
    temps = '&'.join([str(key) + '=' + str(value) for key, value in content.items()])
    temp_split = temps.split("&")
    temp_sort = sorted(temp_split)
    result = '&'.join(temp_sort)
    return result
