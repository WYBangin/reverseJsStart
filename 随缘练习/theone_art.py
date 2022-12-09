import json

import requests
import execjs


def js_from_file(file_name):
    with open(file_name, 'r', encoding="utf-8") as file:
        result = file.read()
    return result


js_func = execjs.compile(js_from_file(r'./theone_art.js'))


def get_sig():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
    encrypt_txt = requests.get("https://api.theone.art/market/api/key/get", headers=headers).json()["data"]
    return js_func.call("get_sig", encrypt_txt)


def main():
    sig = get_sig().strip("=")
    print("当前sig: ", sig)
    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'sig': '{}%3D%3D'.format(sig),
    }

    data = {
        "authorId": None,
        "chainContract": None,
        "commodityCategoryId": None,
        "commodityCategoryIdList": [],
        "commodityId": None,
        "highPrice": "",
        "lowPrice": "",
        "pageCount": 1,
        "pageSize": 20,
        "seriesWorks": None,
        "seriesWorksId": None,
        "sort": {
            "field": 2,
            "upOrDown": 1
        },
        "statusSell": 1,
        "topicId": None,
        "typeMarket": 1,
        "commodityTraitList": [],
        "sig": sig,
    }

    response = requests.post('https://api.theone.art/market/api/saleRecord/list/v2', headers=headers,
                             data=json.dumps(data))
    print(response.text)


if __name__ == '__main__':
    main()

# 目标网站:  aHR0cHM6Ly93d3cudGhlb25lLmFydC9tYXJrZXQ/dHlwZT1jb3B5cmlnaHQ=
