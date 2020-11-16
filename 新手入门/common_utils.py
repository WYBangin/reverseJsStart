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
    encrypt_dict = dict(sorted(encrypt_dict.items(), key=lambda e: e[0]))  # 字典排序
    return encrypt_dict


def params_join(content):
    """字典转换成字符串的函数"""
    temps = '&'.join([str(key) + '=' + str(value) for key, value in content.items()])
    temp_split = temps.split("&")
    temp_sort = sorted(temp_split)
    result = '&'.join(temp_sort)
    return result


def byte_array_to_str(ls, num=8):
    """字节数组转成字符串的函数 2位字节数+(2**8)256将负数变成正数, 8位字节则需要加2**(8*4)"""
    new_ls = [i + 2 ** num if i < 0 else i for i in ls]
    return ''.join(['%02x' % b for b in new_ls])


