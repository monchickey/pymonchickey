# -*- coding: utf-8 -*-
import os, sys
import hashlib
import binascii

# 目录或文件读写操作工具类
class FileIOUtils(object):

    # 递归创建目录，创建成功返回true，已存在返回false
    # 传入参数最好填写绝对路径
    def create_dirs(self, path):
        if os.path.exists(path) == True:
            return False
        else:
            os.makedirs(path)
            return True
    # 读取文件所有内容 二进制安全
    def read_file(self, filename):
        fp = open(filename, 'rb')
        text_content = fp.read()
        fp.close()
        return text_content
    # 向文件中写入新的内容 覆盖原有所有的内容
    def write_file(self, filename, text_content):
        fp = open(filename, 'wb')
        fp.write(text_content)
        fp.close()

    # 向文件末尾指针追加内容
    def add_file_content(self, filename, text_content):
        fp = open(filename, "ab")
        fp.write(text_content)
        fp.close()

    # 获取指定目录下的文件列表 (只遍历一层，不是全遍历)
    def get_files(self, dir_path):
        return os.listdir(dir_path)

    # 读取文件内容为底层16进制字符串 二进制安全
    # filename 文件uri
    # offset_number 偏移量 默认是0读取全部 否则读取指定字节
    def read_file_hex(self, filename, offset_number=0):
        fp = open(filename, 'rb')
        fp.seek(0, 0)
        file_hex_result = ""
        now_offset = 0
        while True:
            byte = fp.read(1)
            if byte == '':
                break
            elif now_offset >= offset_number and offset_number != 0:
                break
            else:
                file_hex_result += byte.encode('hex')
            now_offset += 1
        fp.close()
        return file_hex_result

    # 获取文件的md5 适用于大文件
    def get_file_md5(self, filename):
        if not os.path.isfile(filename):
            return None
        md5_hash = hashlib.md5()
        fp = open(filename, 'rb')
        while True:
            bytes = fp.read(4096)
            if not bytes:
                break
            md5_hash.update(bytes)
        fp.close()
        return md5_hash.hexdigest()

    # 获取文件的sha1指纹 适用于大文件
    def get_file_sha1(self, filename):
        if not os.path.isfile(filename):
            return None
        sha1_hash = hashlib.sha1()
        fp = open(filename, 'rb')
        while True:
            bytes = fp.read(4096)
            if not bytes:
                break
            sha1_hash.update(bytes)
        fp.close()
        return sha1_hash.hexdigest()

    # 这个方法是将文件全部加载到内存然后计算 所以不适用于大文件crc校验
    def get_file_crc32(self, filename):
        if not os.path.isfile(filename):
            return None
        fp = open(filename, 'rb')
        crc32_code = binascii.crc32(fp.read())
        fp.close()
        return '%x' % (crc32_code & 0xffffffff)

