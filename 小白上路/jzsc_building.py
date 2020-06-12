#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/6/11 17:29
# @Author  : 伯明
# @Site    : 
# @File    : jzsc_building.py
# @Software: PyCharm
import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

import requests
from Crypto.Cipher import AES


# 可调用js执行解密方法，如果报错，可参考https://blog.csdn.net/kwoky/article/details/104841611(记得改回来，否则pip安装依赖可能报错)
# python解密版本  包含对应的js版本
class EncryptDate:
    def __init__(self, data):
        self.key = bytes("jo8j9wGw%6HbxfFn", encoding="utf-8")  # 网站密钥
        self.iv = bytes("0123456789ABCDEF", encoding="utf-8")  # 不足16位时补充的字符串
        self.unpad = lambda date: date[0:-ord(date[-1])]  # 不足16位时填充函数
        self.data = bytes.fromhex(data)

    def decrypt(self):  # 解密函数
        aes_obj = AES.new(self.key, AES.MODE_CBC, self.iv)
        decrypt_data = aes_obj.decrypt(self.data)
        result = self.unpad(str(decrypt_data, encoding="utf-8"))
        return result


def buildings():
    url = "http://jzsc.mohurd.gov.cn/api/webApi/dataservice/query/staff/list?pg=0&pgsz=15&orderby=time"

    payload = {}
    headers = {
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'timeout': '30000',
        'accessToken': '',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
        'Referer': 'http://jzsc.mohurd.gov.cn/home',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code == 200:
        data = response.text
        eg = EncryptDate(data)
        json_data = eg.decrypt()
        print(json_data)


if __name__ == '__main__':
    buildings()
