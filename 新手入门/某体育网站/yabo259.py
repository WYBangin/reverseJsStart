#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/8/7 14:23
# @Author  : wyb
# @Site    : 
# @File    : yabo259.py
# @Software: PyCharm
import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

import requests
import hmac
import time
from 新手入门.encrypt_utils import *


def get_nonce_str(n=11):
    """随机生成n位字符串"""
    random_str = "0123456789abcdefghijklmnopqrstuvwxyz"
    nonce_str = ""
    while True:
        nonce_str += random.choice(random_str)
        if nonce_str[0] == "0":
            nonce_str = nonce_str[1:]
        if len(nonce_str) == n:
            break
    return nonce_str


def get_sign(payload):
    encrypt_str = bs64_encode(payload)
    app_securit = "d77f7fcff637bc61bfb82fcbcd767bfa"
    return hmac.new(bytes(app_securit, 'latin-1'), msg=bytes(bs64_encode(encrypt_str), 'latin-1'), digestmod=hashlib.sha256).hexdigest()


def yabo_login(user_name, password):
    """
    某体育网站登录
    :param user_name: 账号
    :param password: 密码
    :return:
    """
    url = "aHR0cDovL3d3dy55YWJvMjU5LmNvbS9tZW1iZXIvdjIvd2ViX2xvZ2lu"
    ts = str(time.time()).split(".")[0]
    nonce_str = get_nonce_str()
    payload_old = "appKey=c97823e281c071c39e&domain=www.yabo259.com&name={}&nonce_str={}&password={}&timestamp={}&uuid=web-Windows-c2bbdeff48455c74599ee6cb02be2d91&appSecurit=d77f7fcff637bc61bfb82fcbcd767bfa".format(user_name, nonce_str, password, ts)
    sign = get_sign(payload_old)
    payload_new = payload_old + "&sign=" + sign
    print("nonce_str: ", nonce_str)
    print("sign:", sign)
    headers = {
        'authority': 'www.yabo259.com',
        'x-api-token': '',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
        'client-type': 'web',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'origin': 'https://www.yabo259.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.yabo259.com/login',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': 'ser=a03; visid_incap_2214260=V5mKq7dFSsCuZ81JG988oD/GLF8AAAAAQUIPAAAAAAAHqnabaO+0jNGxBnv0AIqu; nlbi_2214260=l1oSXIvOYgmBVhLg5kyHlQAAAAD+HLTEDfRR6k1IjkIdlqHX; incap_ses_266_2214260=nJwCQl0OTDZ5GfQiwQWxAz/GLF8AAAAA3RBvivC7uytxJNf5IU/qhw==; live_base_url=https%3A//videos.1ky5dz.com; appurl=%7B%22agent_app_domain%22%3A%22https%3A//www.izhuangyang.com%22%2C%22agent_pc_domain%22%3A%22https%3A//agent.ybagent10.com%22%2C%22app_domain%22%3A%22https%3A//www.yb446.app%22%2C%22customer_download%22%3A%22%22%2C%22h5_domain%22%3A%22https%3A//www.yabo393.com%22%2C%22site_domain%22%3A%22https%3A//www.yabovip2027.com%22%2C%22sport_domain%22%3A%22https%3A//www.yb73.app%22%7D; app_domain=https%3A//www.yb446.app; sport_domain=https%3A//www.yb73.app; h5_domain=https%3A//www.yabo393.com; zg_did=%7B%22did%22%3A%20%22173c6e68961c9-04be5b1f814f3f-5d462912-1fa400-173c6e68962163%22%7D; _ga=GA1.2.208900397.1596769864; _gid=GA1.2.75772918.1596769864; _gat_gtag_UA_138682257_1=1; zg_56bafcb9a97a461284175f0b080c931c=%7B%22sid%22%3A%201596769864044%2C%22updated%22%3A%201596769884959%2C%22info%22%3A%201596769864058%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22landHref%22%3A%20%22https%3A%2F%2Fwww.yabo259.com%2Flogin%22%7D; _0x17e684=zvmns1wihsr; ser=a03; incap_ses_266_2214260=sFFcbQ4hG1zTIUwjwQWxAzfzLF8AAAAAt9WJXdbuEI4SW+/DOWNz9A=='
    }
    print(bs64_decode(url))
    response = requests.post(bs64_decode(url), headers=headers, data=payload_new)
    return response.content.decode()


if __name__ == '__main__':
    print(yabo_login("admin", "123456"))