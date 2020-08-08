import hashlib
import base64
import hmac
import random
from urllib.parse import unquote


def md5(content):
    return hashlib.md5(content.encode("utf-8")).hexdigest()


def bs64_decode(content):
    return unquote(base64.b64decode(content).decode("utf-8"))


def bs64_encode(content):
    return bytes.decode(base64.b64encode(content.encode("utf-8")))


def hmac_sha256(encrypt_str, key):
    return hmac.new(bytes(key, 'latin-1'), msg=bytes(encrypt_str, 'latin-1'), digestmod=hashlib.sha256).hexdigest()


if __name__ == "__main__":
    print(bs64_encode("http://www.yabo259.com/member/v2/web_login"))

"""
hmac加密方式
API_SECRET = 'd77f7fcff637bc61bfb82fcbcd767bfa'
bb = "appKey=c97823e281c071c39e&domain=www.yabo259.com&name=test&nonce_str=buty8497uac&password=123456&timestamp=1596770111&uuid=web-Windows-c2bbdeff48455c74599ee6cb02be2d91&appSecurit=d77f7fcff637bc61bfb82fcbcd767bfa"
print(hmac.new(bytes(API_SECRET, 'latin-1'), msg=bytes(bs64_encode(bb), 'latin-1'), digestmod=hashlib.sha256).hexdigest())
"""
