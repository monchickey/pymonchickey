# -*- coding: utf-8 -*-
import os
import sys
import hashlib
import binascii

class FileIOUtils(object):
    """目录或文件读写以及操作工具类
    """

    def create_dirs(self, path):
        """递归创建目录
        Args:
            path: 要创建的目录路径, 最好是写绝对路径
        Returns:
            返回类型: 布尔值
            创建成功: True
            目录已存在返回: False
        """
        if os.path.exists(path):
            return False
        else:
            os.makedirs(path)
            return True

    def delete_path(self, path):
        """递归删除指定路径
        同时适用于文件或目录, 如果是目录则删除目录及下面的所有文件
        Args:
            path: 要删除的路径
        """
        if os.path.isdir(path):
            for deep_path in os.listdir(path):
                # 递归调用删除方法
                self.delete_path(os.path.join(path, deep_path))
            if os.path.exists(path):
                os.rmdir(path)
        else:
            if os.path.exists(path):
                os.remove(path)

    def read_file(self, filename):
        """读取文件所有内容并返回
        二进制安全
        """
        fp = open(filename, 'rb')
        file_content = fp.read()
        fp.close()
        return file_content
    
    def write_file(self, filename, file_content):
        """向文件中写入新的内容
        会覆盖原有所有的内容, 二进制安全
        """
        fp = open(filename, 'wb')
        fp.write(file_content)
        fp.close()

    def add_file_content(self, filename, file_content):
        """从文件末尾指针开始追加内容
        二进制安全
        """
        fp = open(filename, "ab")
        fp.write(file_content)
        fp.close()


    def get_files(self, dir_path):
        """获取指定目录下的文件列表
        只遍历一层, 不是全遍历
        """
        return os.listdir(dir_path)

    
    def read_file_hex(self, filename, offset_number=0):
        """读取文件内容为底层数据的16进制字符串形式,二进制安全
        Args:
            filename: 文件路径
            offset_number: 偏移量
                默认值为: 0  表示读取全部
                否则读取指定个字节的内容
        Returns:
            返回读取内容的16进制字符串形式
        """
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

    
    def get_file_md5(self, filename):
        """获取文件的md5值
        同样适用于大文件
        Args:
            filename: 文件位置
        Returns:
            如果文件存在, 返回文件的md5值
            如果文件不存在或路径不是文件, 返回None
        """
        if not os.path.isfile(filename):
            return None
        md5_hash = hashlib.md5()
        fp = open(filename, 'rb')
        while True:
            tmp_bytes = fp.read(4096)
            if not tmp_bytes:
                break
            md5_hash.update(tmp_bytes)
        fp.close()
        return md5_hash.hexdigest()


    def get_file_sha1(self, filename):
        """获取文件的sha1指纹
        同样适用于大文件
        Args:
            filename: 文件位置
        Returns:
            如果文件存在, 返回文件的sha1值
            如果文件不存在或路径不是文件, 返回None
        """
        if not os.path.isfile(filename):
            return None
        sha1_hash = hashlib.sha1()
        fp = open(filename, 'rb')
        while True:
            tmp_bytes = fp.read(4096)
            if not tmp_bytes:
                break
            sha1_hash.update(tmp_bytes)
        fp.close()
        return sha1_hash.hexdigest()

    
    def get_file_crc32(self, filename):
        """获取文件的CRC32校验码
        这里将文件全部加载到内存然后计算, 所以不适用于大文件
        Args:
            filename: 文件位置
        Returns:
            如果文件存在, 返回文件的CRC32值
            如果文件不存在或路径不是文件, 返回None
        """
        if not os.path.isfile(filename):
            return None
        fp = open(filename, 'rb')
        crc32_code = binascii.crc32(fp.read())
        fp.close()
        return '%x' % (crc32_code & 0xffffffff)

