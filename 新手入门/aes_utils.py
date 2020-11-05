import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

import base64
from Crypto.Cipher import AES


class AESTool(object):
    """AES工具类 这里是CBC模式"""

    def __init__(self, key, iv, mode=AES.MODE_CBC):
        """
        初始方法
        :param data: 要加密数据
        :param key: 秘钥
        :param iv: 便偏移量
        :param mode: 加密方式
        """
        self.key = key.encode("utf-8")
        self.iv = iv.encode("utf-8")
        self.mode = mode

    def base64_aes_encrypt(self, data):
        """输出结果为base64"""
        pad = lambda s: s + (16 - len(s) % 16) * chr(16 - len(s) % 16)  # 定义一个函数，这个函数的名字pad，这个函数需要一个参数，也就是s。
        data = pad(data)  # CBC模式AES加密需要满足加密数据长度是密钥长度的整数倍，所以如果长度不是整数倍，要加数据
        cipher = AES.new(self.key, self.mode, self.iv)
        encrypt_data = cipher.encrypt(data.encode('utf8'))
        encode_str = base64.b64encode(encrypt_data)
        enc_text = encode_str.decode('utf8')  # 对byte字符串按utf-8进行解码
        return enc_text

    def base64_aes_decrypt(self, data):
        """解密base64格式数据"""
        unpad = lambda s: s[0:-s[-1]]
        data = data.encode('utf8')  # 转成byte字符串
        encode_bytes = base64.decodebytes(data)
        cipher = AES.new(self.key, self.mode, self.iv)
        text_decrypted = cipher.decrypt(encode_bytes)
        # CBC模式AES加密需要满足加密数据长度是密钥长度的整数倍，所以数据后面可能有不需要的后来添加的数据，所以我们就去掉
        # 添加后缀的时候按照“16 - len(s)%16”，那么后面那个字符的码值也就是原串原来长度差了多少是16整数倍
        text_decrypted = unpad(text_decrypted)
        text_decrypted = text_decrypted.decode('utf8')
        return text_decrypted

    def hex_aes_encrypt(self, data):
        """输出结果为hex格式"""
        pad = lambda s: s + (16 - len(s) % 16) * chr(16 - len(s) % 16)  # 定义一个函数，这个函数的名字pad，这个函数需要一个参数，也就是s。
        data = pad(data)  # CBC模式AES加密需要满足加密数据长度是密钥长度的整数倍，所以如果长度不是整数倍，要加数据
        cipher = AES.new(self.key, self.mode, self.iv)
        encrypt_data = cipher.encrypt(data.encode('utf8'))
        enc_text = encrypt_data.hex()
        return enc_text

    def hex_aes_decrypt(self, data):
        """解密hex格式数据"""
        unpad = lambda s: s[0:-s[-1]]
        encode_bytes = bytes.fromhex(data)
        cipher = AES.new(self.key, self.mode, self.iv)
        text_decrypted = cipher.decrypt(encode_bytes)
        text_decrypted = unpad(text_decrypted)
        text_decrypted = text_decrypted.decode('utf8')
        return text_decrypted


if __name__ == '__main__':
    kk = "20171109124536982017110912453698"
    vv = "2017110912453698"
    aes_obj = AESTool(kk, vv)
    print(aes_obj.base64_aes_encrypt("test"))
    print(aes_obj.hex_aes_encrypt("test"))
