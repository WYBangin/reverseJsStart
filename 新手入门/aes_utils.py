import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


class AESToolCBC(object):
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
        encode_bytes = base64.decodebytes(data.encode('utf8'))
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


class AESToolECB(object):
    """AES工具类 这里是ECB模式"""

    def __init__(self, key, mode=AES.MODE_ECB):
        """
        初始方法
        :param data: 要加密数据
        :param key: 秘钥
        :param iv: 便偏移量
        :param mode: 加密方式
        """
        self.key = key.encode("utf-8")
        self.mode = mode
        self.unpad = lambda s: s[0:-ord(s[-1])]  # 截断函数

    def fill_method(self, aes_str):
        """pkcs7补全函数"""
        pad_pkcs7 = pad(aes_str.encode('utf-8'), AES.block_size, style='pkcs7')
        return pad_pkcs7

    def base64_aes_encrypt(self, data):
        """输出结果为base64"""
        cipher = AES.new(self.key, self.mode)
        result = cipher.encrypt(self.fill_method(data))
        enc_text = str(base64.b64encode(result), encoding="utf-8")
        return enc_text

    def base64_aes_decrypt(self, data):
        """解密base64格式数据"""
        cipher = AES.new(self.key, self.mode)
        encode_bytes = base64.decodebytes(data.encode('utf8'))
        text_decrypted = cipher.decrypt(encode_bytes)
        decrypt_text = self.unpad(text_decrypted.decode('utf8'))
        return decrypt_text

    def hex_aes_encrypt(self, data):
        """输出结果为hex格式"""
        cipher = AES.new(self.key, self.mode)
        result = cipher.encrypt(self.fill_method(data))
        enc_text = result.hex()
        return enc_text

    def hex_aes_decrypt(self, data):
        """解密hex格式数据"""
        cipher = AES.new(self.key, self.mode)
        encode_bytes = bytes.fromhex(data)
        text_decrypted = cipher.decrypt(encode_bytes)
        decrypt_text = self.unpad(text_decrypted.decode('utf8'))
        return decrypt_text

    
if __name__ == '__main__':
    kk = "20171109124536982017110912453698"
    vv = "2017110912453698"
    aes_obj = AESToolCBC(kk, vv)
    print("CBC加密: ", aes_obj.base64_aes_encrypt("test"))
    print("CBC解密: ", aes_obj.hex_aes_encrypt("test"))
    new_key = '1650097882000123'
    msg = '1234567890abcdefghijklmnopqrstuvwxyz'
    aes_ecb = AESToolECB(new_key)
    aes_result = aes_ecb.hex_aes_encrypt(msg)
    print("ECB加密: ", aes_result)
    print("ECB解密: ", aes_ecb.hex_aes_decrypt(aes_result))
