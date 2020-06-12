#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/6/12 11:32
# @Author  : 伯明
# @Site    : 
# @File    : person_bank_detail.py
# @Software: PyCharm
import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# 某银行公告页面, js动态生成重定向的url (注：可更换请求方式)
import requests
import re
import execjs


def get_url(s, headers):
    """
    获取解密后的部分url
    :param s:
    :param headers:
    :return:
    """
    url_1 = 'http://www.pbc.gov.cn/tiaofasi/144941/144957/index.html'
    response = s.get(url_1, headers=headers)
    js = re.findall('<script type="text/javascript">(.*?)</script>', response.content.decode(), re.S | re.M)[0]
    ll = re.sub("window\[_0x56ae\('0x3c','\)9A&'\)\]=_0x35ace3;", "return _0x35ace3;", js)
    ctx = execjs.compile(ll)
    href = ctx.call('_0x33f22a')
    print("解密后的url: ", href)
    return href


def main():
    s = requests.session()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36',
    }

    href = get_url(s, headers)
    url = "http://www.pbc.gov.cn" + href
    response = s.get(url=url, headers=headers)
    html = response.content.decode()
    if "银行" in html:
        print("success")  # 有银行字样证明解密成功
    else:
        print("failed")


if __name__ == '__main__':
    main()
