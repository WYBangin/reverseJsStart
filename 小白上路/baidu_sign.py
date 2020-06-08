#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/6/4 18:18
# @Author  : 伯明
# @Site    : 
# @File    : baidu_sign.py
# @Software: PyCharm
import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

import requests
import re
import json
import execjs

with open(r"./baidu_now.js", "r", encoding='utf8') as f:
    js = f.read()
ctx = execjs.compile(js)


def baidu_translate():
    while True:
        words = input("请输入要查询的内容, 输入 ## 退出：")
        if words == "##":
            print("退出程序成功！！！")
            break
        url = "https://fanyi.baidu.com/v2transapi"
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
            "cookie": "BIDUPSID=E899030A6BC72DC81FAE9502179FD90A; PSTM=1587884465; BAIDUID=E899030A6BC72DC883396EB1C9EAB672:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=31657_1455_31670_21089_31069_31660_31762_30824_31848_26350; delPer=0; PSINO=7; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1591263222; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; yjs_js_security_passport=368b305306a146294048e6a402cc43faf28fd188_1591264942_js; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1591265587; __yjsv5_shitong=1.0_7_431a7917dfed8a0d423979aa61a8d722937b_300_1591265588678_112.94.22.95_5342a6de",
        }
        zh_en = re.compile('[\u4e00-\u9fa5]+')  # 判断输入的内容中是否有中文
        if re.search(pattern=zh_en, string=words):
            fr = "zh"
            to = "en"
        else:
            fr = "en"
            to = "zh"

        sign = ctx.call("e", str(words))
        data = {
            "from": fr,
            "to": to,
            "query": words,
            "transtype": "translang",
            "simple_means_flag": "3",
            "sign": sign,
            "token": "9c369573d0bb14f22758aeb51c6506d8",    # token对应i的值
        }
        res = requests.post(url, data=data, headers=headers)
        translate = json.loads(res.text)
        try:
            print('query:', words, '\r\n', 'translate_result:', translate["trans_result"]["data"][0]["dst"])
        except Exception as e:
            print("返回结果有误，请检查")


if __name__ == "__main__":
    baidu_translate()
    # http://fanyi.youdao.com/
