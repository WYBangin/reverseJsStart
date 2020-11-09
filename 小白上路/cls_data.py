#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/11/9 16:47
# @Author  : wyb
# @Site    : 
# @File    : cls_data.py 某联社主页网站sign
# @Software: PyCharm
import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

import requests
import time

from 新手入门.encrypt_utils import md5, hmac_sha1


# 目标网站 aHR0cHM6Ly93d3cuY2xzLmNuL3RlbGVncmFwaA==

def params_sort(content):
    """字符串排序"""
    encrypt_list = [each for each in content.split('&') if "sign" not in each]
    temp_sort = sorted(encrypt_list)
    result = '&'.join(temp_sort)
    return result


def get_sign(source_url):
    encrypt_str = source_url[source_url.index('?') + 1:]
    return md5(hmac_sha1(encrypt_str))


def get_roll_list():
    url = "https://www.cls.cn/v1/roll/get_roll_list?app=CailianpressWeb&category=jpush&last_time={}&os=web&refresh_type=1&rn=20&sv=7.2.2".format(
        int(time.time()))
    sign = get_sign(url)
    print("获取sign: ", sign)
    target_url = url + "&sign=" + sign
    payload = {}
    headers = {
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
        'Content-Type': 'application/json;charset=utf-8',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.cls.cn/telegraph',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': 'HWWAFSESID=4d99da9ede9500e5a9; HWWAFSESTIME=1604910723785; hasTelegraphNotification=on; hasTelegraphRemind=on; hasTelegraphSound=on; vipNotificationState=on; Hm_lvt_fa5455bb5e9f0f260c32a1d45603ba3e=1603092968,1604555395,1604910728; Hm_lpvt_fa5455bb5e9f0f260c32a1d45603ba3e=1604913124'
    }

    response = requests.get(target_url, headers=headers, data=payload)
    print(response.text)


if __name__ == '__main__':
    for i in range(2):
        get_roll_list()
