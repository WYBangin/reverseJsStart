#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/11/16 11:48
# @Author  : wyb
# @Site    : 
# @File    : china_news.py
# @Software: PyCharm
import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# 中新网 accesstoken  网址: aHR0cHM6Ly9tLmNoaW5hbmV3cy5jb20vd2FwL3piL2Nocw
import requests
import time

from 新手入门.encrypt_utils import md5
from 新手入门.common_utils import params_to_dict


def main():
    now_time = str(time.time()*1000).split(".")[0]
    url = "https://m.chinanews.com/chinanews/getLiveList?language=chs&dtp=3&isWap=yes&pageIndex=1&version_chinanews=6.7.8"
    params = url[url.index("?") + 1:]
    sort_str = params + "&appKey={}&appSecret={}&timestrap={}".format("CNSAPP", "NJAGTABQ", now_time)
    encrypt_dict = params_to_dict(sort_str)
    encrypt_str = "".join([v for k, v in encrypt_dict.items()])
    payload = {}
    headers = {
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'timestamp': now_time,
        'accessToken': md5(encrypt_str),
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
        'appKey': 'CNSAPP',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://m.chinanews.com/wap/zb/chs',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        # 'Cookie': '__jsluid_s=75624de9a03bc6793d2b58a053fc9967'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)


if __name__ == '__main__':
    main()
