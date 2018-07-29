# -*- coding: utf-8 -*-
"""目录或文件读写等操作工具类"""
import os
import sys
import hashlib
import binascii

def create_dirs(path):
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

def delete_path(path):
    """递归删除指定路径
    同时适用于文件或目录, 如果是目录则删除目录及下面的所有文件
    Args:
        path: 要删除的路径
    """
    if os.path.isdir(path):
        for deep_path in os.listdir(path):
            # 递归调用删除方法
            delete_path(os.path.join(path, deep_path))
        if os.path.exists(path):
            os.rmdir(path)
    else:
        if os.path.exists(path):
            os.remove(path)

def read_file(filename):
    """读取文件所有内容, 并返回为字符串
    二进制安全
    """
    fp = open(filename, 'rb')
    file_content = fp.read()
    fp.close()
    return file_content
    
def write_file(filename, file_content):
    """向文件中写入新的内容
    如果文件存在会覆盖原有所有的内容, 支持二进制
    """
    fp = open(filename, 'wb')
    fp.write(file_content)
    fp.close()

def file_append_content(filename, file_content):
    """从文件末尾指针开始追加内容
    二进制安全
    """
    fp = open(filename, "ab")
    fp.write(file_content)
    fp.close()


def get_files(dir_path):
    """获取指定目录下的文件列表 (包括文件和目录)
    只遍历一层
    """
    return os.listdir(dir_path)

    
def read_file_hex(filename, byte_number=0):
    """读取文件数据并以16进制的字符串形式返回
    Args:
        filename: 文件路径
        byte_number: 读取字节个数
            默认值为: 0  表示读取全部
            否则读取指定个字节的内容
    Returns:
        返回读取内容的16进制字符串形式
    """
    fp = open(filename, 'rb')
    fp.seek(0, 0)
    file_hex_result = []
    now_offset = 0
    while True:
        r_byte = fp.read(1)
        if not r_byte:
            break
        if now_offset >= byte_number and byte_number != 0:
            break
        file_hex_result.append(r_byte.encode('hex'))
        now_offset += 1
    fp.close()
    return b''.join(file_hex_result)

    
def get_file_md5(filename):
    """计算文件的md5指纹
    适用于大文件
    Args:
        filename: 文件路径
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


def get_file_sha1(filename):
    """计算文件的sha1指纹
    适用于大文件
    Args:
        filename: 文件路径
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

    
def get_file_crc32(filename):
    """获取文件的CRC32校验码
    需要将文件全部加载到内存然后计算, 不适用于大文件
    Args:
        filename: 文件路径
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
