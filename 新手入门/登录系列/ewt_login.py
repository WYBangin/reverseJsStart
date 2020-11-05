#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/11/5 11:25
# @Author  : wyb
# @Site    : 
# @File    : ewt_login.py
# @Software: PyCharm
import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from 新手入门.aes_utils import AESTool
import requests


# 目标网站: AaB+cbTRKO8b82MHz5yRrApoUXvkou6C1UVxl439YvwdkfeIh93CrLlskQYQ3gEag9yfSDqiQCH4sYuZ/vYXnw==
def get_pwd(pwd):
    """加密密码"""
    aes_obj = AESTool("20171109124536982017110912453698", "2017110912453698")
    res = aes_obj.hex_aes_encrypt(pwd)
    return res.upper()


def main_login(user, pwd):
    url = "https://web.ewt360.com/api/authcenter/oauth/login"
    new_pwd = get_pwd(pwd)
    print("加密前密码: ", pwd)
    print("加密后密码: ", new_pwd)

    payload = "{\"platform\":1,\"userName\":\"" + user + "\",\"password\":\"" + new_pwd + "\"}"
    headers = {
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
        'secretId': '2',
        'Accept': 'application/json, text/plain, */*',
        'timestamp': '1604546628106',
        'platform': '1',
        'Content-Type': 'application/json;charset=UTF-8',
        'token': 'undefined',
        # 'sign': 'E710E42EEF71F243413027500857BF29',
        'Origin': 'https://web.ewt360.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        # 'Cookie': 'big_data_cookie_id=956c-f375-084b-ae84-e91e; big_data_cookie_time=1603955071276'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


if __name__ == '__main__':
    print(main_login(user="test ", pwd="test123"))  # 此为测试账号, 去目标网站登录对比即可
