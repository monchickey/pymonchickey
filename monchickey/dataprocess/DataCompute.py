# -*- coding:utf-8 -*-
import base64
import random
import hashlib

#  数据计算类(一般用于做一些计算，统计某些信息，加密等)

class DataCompute(object):
    # 统计所给文本中指定某一单词的个数
    def text_word_number(self, text, word):
        num = 0
        while text.find(word) != -1:
            text = text.replace(word, "", 1)
            num = num + 1
        return num

    # 和上述方法功能一样，实现方式不同
    def text_word_number2(self, text, word):
        num = 0
        for i in range(0,len(text) - len(word) + 1):
            if text[i:i+len(word)] == word:
                num = num + 1
        return num

    # 对字符串进行base64编码 图片读出来之后默认也是字符串
    def base64_encode(self, str_data):
        return base64.b64encode(str_data)

    # base64解码为原始字符串
    def base64_decode(self, base64_str):
        return base64.b64decode(base64_str)

    # 随机生成指定位数的数字密码
    def create_random_number_password(self, number_digits):
        password = []
        for n in range(0, number_digits):
            password.append(str(random.randint(0, 9)))
        return ''.join(password)

    # 字符串的md5 hash生成
    def generate_md5(self, src):
        m = hashlib.md5()
        m.update(src)
        return m.hexdigest()
