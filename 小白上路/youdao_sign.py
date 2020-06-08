#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/6/8 16:07
# @Author  : 伯明
# @Site    : 
# @File    : youdao_sign.py
# @Software: PyCharm
import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

import requests
import hashlib
import time
import random
import json

cookies = {
    'OUTFOX_SEARCH_USER_ID_NCOO': '1773704018.3737588',
    'OUTFOX_SEARCH_USER_ID': '1474062680@10.108.160.18',
    'JSESSIONID': 'aaaeRUTIyqpr09TyA9skx',
    '___rl__test__cookies': '1591603490710',
}


def get_sign(word, salt):
    encry_str = "fanyideskweb" + str(word) + salt + "Nw(nmmbP%A-r6U3EUn]Aj"
    return hashlib.md5(encry_str.encode(encoding="utf-8")).hexdigest()


def get_bv(data):
    return hashlib.md5(data.encode(encoding="utf-8")).hexdigest()


def youdao_translate():
    while True:
        words = input("请输入要查询的内容, 输入 ## 退出：")
        if words == "##":
            print("退出程序成功！！！")
            break
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'http://fanyi.youdao.com',
            'Referer': 'http://fanyi.youdao.com/',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }

        params = (
            ('smartresult', ['dict', 'rule']),
        )
        ts = str(int(time.time()) * 1000)
        salt_time = str(int(ts) + int(random.random() * 10))
        data = {
            'i': words,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': salt_time,
            'sign': get_sign(words, salt_time),
            'ts': ts,
            'bv': get_bv(headers["User-Agent"]),
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME'
        }

        response = requests.post('http://fanyi.youdao.com/translate_o', headers=headers, params=params, cookies=cookies,
                                 data=data, verify=False)
        translate = json.loads(response.text)
        try:
            print('query:', words, '\r\n', 'translate_result:', translate["translateResult"][0][0]["tgt"])
        except Exception as e:
            print("返回结果有误，请检查")


if __name__ == '__main__':
    youdao_translate()
