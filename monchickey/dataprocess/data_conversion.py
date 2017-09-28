# -*- coding:utf-8 -*-

import time
import binascii
import json
import base64

class DataConversion(object):
    """数据转换工具类
    包括数据类型转换,时间转换,json转换,字符串类型转换,base64编解码等
    """

    def time_to_str(self, time_float, time_format):
        """时间戳转时间字符串
        Args:
            time_float: 浮点数类型的时间戳
            time_format: 格式化时间的格式 如:'%Y-%m-%d %H:%M:%S'
        Returns:
            返回指定时间格式的字符串
        """
        return time.strftime(time_format, time.localtime(time_float))

    # 时间字符串转时间戳
    # time_str 时间字符串
    # time_format 解析字符串的格式 比如:'%Y-%m-%d %H:%M:%S'
    def str_to_time(self, time_str, time_format):
        return time.mktime(time.strptime(time_str, time_format))

    # 转换普通字符串为底层十六进制字符串表示 注:这里传入类型必须为字符串 转换后为十六进制的字符串形式
    def str_to_hex(self, str_data):
        return binascii.b2a_hex(str_data)

    # 还原十六进制字符串为普通字符串
    def hex_to_str(self, hex_str):
        return binascii.a2b_hex(hex_str)

    # 转换16进制字符串为整型数字 注:传入参数是16进制字符串 返回为一个整数
    def hex_to_int(self, hex_str):
        return int(hex_str, 16)

    # 转换10进制整数为16进制字符串形式
    def int_to_hex(self, integer_number):
        # int 默认为4个字节 最大值为2^31 - 1也就是0xfffffff 整数为214748367 超过这个数之后将会变为长整型 相应的16进制后面也会带个L
        # 此方法不安全因为不同机器上int长度不同
        # if integer_number <= 2147483647:
        #     return hex(integer_number)[2:]
        # else:
        #     hex_str = hex(integer_number)[2:]
        #     return hex_str[0:len(hex_str) - 1]
        hex_content = hex(integer_number)[2:]
        if 'L' in hex_content:
            return hex_content[:-1]
        return hex_content

    # 转换一个10进制整数为二进制字符串 注:传入参数为整数 返回是二进制的字符串形式
    def int_to_bin(self, integer_number):
        return bin(integer_number)[2:]

    # 转换二进制字符串为10进制数字 注:传入参数是二进制的字符串 返回的是整型的数字
    def bin_to_int(self, bin_str):
        bin_str = '0b' + bin_str
        return int(bin_str, 2)

    # 转换一个底层二进制的字符串形式为其所表示的字符串形式 注:传入参数为二进制字符串 比如:'00101010'
    def bin_to_str(self, bin_str):
        # bin_str = '0b' + bin_str
        # 这里可以使用上面整型转换的方式去读 也可以按位转换成16进制
        fill = len(bin_str) % 4
        if fill == 0:
            hex_str = ""
            for i in range(0, len(bin_str) - 3, 4):
                hex_str = hex_str + hex(int(bin_str[i:i + 4], 2))[2:]
        else:
            fill_bit = (4 - fill)*'0'
            bin_str = fill_bit + bin_str
            hex_str = ""
            for i in range(0, len(bin_str) - 3, 4):
                hex_str = hex_str + hex(int(bin_str[i:i + 4], 2))[2:]
        return hex_str.decode('hex')

    # 转换一个普通的字符串为底层二进制字符串形式 注:传入参数必须为字符串 返回的是二进制的字符串形式
    def str_to_bin(self, str_data):
        str_hex = str_data.encode('hex')
        str_int = int(str_hex, 16)
        return bin(str_int)[2:]

    # [0,255] 闭区间范围内整数转换为ascii字符 注意不要超过范围
    def int_to_ascii(self, integer_number):
        return chr(integer_number)

    # 整数转换为对应的字符串(字节数组) 范围不限
    def int_to_str(self, integer_number):
        # 首先转换整数为十六进制字符串
        hex_str = self.int_to_hex(integer_number)
        return self.hex_to_str(hex_str)

    def json_parse(self, json_str):
        """解析json字符串为内置字典(包括嵌套字典或列表)结构
        Args:
            json_str: json交换格式的字符串
        Returns:
            解析成功返回结果
            解析异常返回None
        """
        try:
            return json.loads(json_str)
        except Exception as e:
            return None

    def convert_to_json(self, data):
        """转换内置字典结构(包括嵌套字典或列表等数据结构)为json交换格式的字符串
        Args:
            data: 内置数据结构
        Returns:
            返回转换好的json字符串
        """
        return json.dumps(data, skipkeys=True)

    def base64_encode(self, str_data):
        """对字符串进行base64编码
        方法二进制安全 比如图片读出来之后默认也是字符串
        """
        return base64.b64encode(str_data)

    def base64_decode(self, base64_str):
        """base64字符串解码为原始字符串"""
        return base64.b64decode(base64_str)
