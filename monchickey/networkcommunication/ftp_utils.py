# coding=utf-8
from ftplib import FTP

class FTPUtils(object):
    """ftp文件工具类"""

    # ftp连接操作
    def __init__(self, ipaddr, port, username, password):
        self.ipaddr = ipaddr
        self.port = int(port)
        self.username = username
        self.password = password

    # 下载远程ftp文件 (路径全部使用完整的绝对路径)
    def download_file(self, remote_file, local_file):
        ftp = FTP()
        # ftp.set_debuglevel(2) 设置ftp debug级别 默认为0
        try:
            ftp.connect(self.ipaddr, self.port)
        except Exception, e:
            # 连接ftp服务器失败
            return -1
        try:
            ftp.login(self.username, self.password)
        except Exception, e:
            # 登录ftp服务器失败
            return -2
        # 连接成功 开始下载
        bufsize = 1024 # 设置缓冲区大小
        try:
            fp = open(local_file, 'wb')
            ftp.retrbinary('RETR %s' % remote_file, fp.write, bufsize)
        except Exception, e:
            # 保存文件异常
            return -3
        finally:
            fp.close()
            ftp.quit()
        # 保存文件成功
        return 0

    # 上传本地文件到远程ftp服务器 (使用绝对路径)
    def upload_file(self, local_file, remote_file):
        ftp = FTP()
        # ftp.set_debuglevel(2) 设置ftp debug级别 默认为0
        try:
            ftp.connect(self.ipaddr, self.port)
        except Exception, e:
            # 连接ftp服务器失败
            return -1
        try:
            ftp.login(self.username, self.password)
        except Exception, e:
            # 登录ftp服务器失败
            return -2
        # 连接成功 开始下载
        bufsize = 1024 # 设置缓冲区大小
        try:
            fp = open(local_file, 'rb')
            ftp.storbinary('STOR %s' % remote_file, fp, bufsize)
        except Exception, e:
            # 保存文件异常
            return -3
        finally:
            fp.close()
            ftp.quit()
        # 保存文件成功
        return 0


