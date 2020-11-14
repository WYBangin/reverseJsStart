#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/11/14 17:39
# @Author  : wyb
# @Site    : 
# @File    : hrdj.py
# @Software: PyCharm
import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# 某点集短视频网站 aHR0cHM6Ly9keS5ocmRqeXVuLmNvbS8/Iy9yYW5rbGlzdC9yZWFsVGltZUxpdmU=

import requests
import time
import json
from 新手入门.encrypt_utils import sha256


def get_sign(params, ts):
    """生成sign"""
    content = 'param={}&timestamp={}&tenant=1&salt=kbn%&)@<?FGkfs8sdf4Vg1*+;`kf5ndl$'.format(params, ts)
    result = sha256(content)
    return result


def main():
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
        'Content-Type': 'application/json;charset=UTF-8',

    }
    params = {"no": "dy0002", "data": {"days": 1, "rankType": 7}}
    ts = str(time.time() * 1000).split(".")[0]
    sign = get_sign(params, ts)
    print("生成sign: ", sign)
    data = '{"param": "' + str(
        params) + '","sign":"' + sign + '","tenant":"1","timestamp":"' + ts + '","token":"WCuHTHDgl/xsuzMlLcwbq4Bc4OkLEF5c8/aVE/DUerJQT+KYZEtqzTYjoEvmU+R2TaWSrUhfWk4d\\nvKRTKS1sV4C+/X0JAJ4kElqT9f3+rAVssvG3vIy87a4a+VOrP555QhS4nJNUp0Z2AFY9hSCyYaTa\\nDz8Ea6wZEwdBamWIi5SDniLJf3+eYRfhaKoYOd0Jyol6Uw4uqobCowaxX2I+jmGd+pvFTEKalTAk\\nc5WgIoHdtKJ0m+9gLh2Jr9v5GWKvJNJ6JqDbdSrALJ9IMR0Amw=="}'
    response = requests.post('https://ucp.hrdjyun.com:60359/api/dy', headers=headers, data=data)
    print(response.text)


if __name__ == '__main__':
    main()
