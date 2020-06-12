#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/6/12 17:34
# @Author  : 伯明
# @Site    : 
# @File    : qimingpian.py
# @Software: PyCharm
import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

import requests
import json
import execjs

with open(r"./qimingpian.js", "r", encoding='utf8') as f:
    js = f.read()
ctx = execjs.compile(js)


def decrypt_data(data):
    json_data = ctx.call("decrypt", data)
    return json_data


def main():
    url = "https://vipapi.qimingpian.com/DataList/productListVip"

    payload = 'time_interval=&tag=&tag_type=&province=&lunci=&page=1&num=20&unionid='
    headers = {
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://www.qimingpian.cn',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code:
        json_data = json.loads(response.text)
        encrypt_data = json_data["encrypt_data"]
        product_info = decrypt_data(encrypt_data)
        print("解密数据是: ", json.loads(product_info))
    else:
        print("获取数据失败")


if __name__ == '__main__':
    main()

# https://www.qimingpian.cn/finosda/project/pinvestment 某名片网站
