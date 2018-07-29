# coding=utf-8
import os
import logging
from ftplib import FTP

class FTPUtil(object):
    """ftp文件操作工具"""

    def __init__(self, ipaddr, port, username, password):
        self.ipaddr = ipaddr
        self.port = int(port)
        self.username = username
        self.password = password

        self.log = logging.getLogger(__name__)

    def download_file(self, remote_file, local_file):
        """下载远程ftp文件 (路径请全部使用完整的绝对路径)
        Args:
            remote_file: 要下载的远程文件路径
            local_file: 保存到本地文件的路径
        Returns:
            0 - 下载成功.
            -1 - ftp服务器连接失败.
            -2 - ftp服务器登录失败
            -3 - 下载或保存文件异常.
        """
        ftp = FTP()
        # 设置ftp debug级别, 默认为0
        # ftp.set_debuglevel(2)
        try:
            ftp.connect(self.ipaddr, self.port)
        except Exception as e:
            self.log.error("Connection to ftp server failed! {}".format(e))
            return -1
        try:
            ftp.login(self.username, self.password)
        except Exception as e:
            self.log.error("Login to ftp server failed! {}".format(e))
            return -2
        # 设置缓冲区大小
        bufsize = 4096
        try:
            fp = open(local_file, 'wb')
            ftp.retrbinary('RETR %s' % remote_file, fp.write, bufsize)
        except Exception as e:
            self.log.error("Download file exception! {}".format(e))
            return -3
        finally:
            fp.close()
            ftp.quit()
        return 0

    def upload_file(self, local_file, remote_file):
        """上传本地文件到远程ftp服务器
        Args:
            local_file: 本地文件路径
            remote_file: 上传到ftp远程路径
                注意: 如果远程目录不存在, 则上传会出错, 不会自动建立目录
        Returns:
            0 - 上传成功.
            -1 - ftp服务器连接失败.
            -2 - ftp服务器登录失败
            -3 - 上传文件异常.
            -4 - 本地文件不存在.
        """
        if not os.path.isfile(local_file):
            self.log.warning("Local file {} does not exist!".format(local_file))
            return -4
        ftp = FTP()
        # ftp.set_debuglevel(2)
        try:
            ftp.connect(self.ipaddr, self.port)
        except Exception as e:
            self.log.error("Connection to ftp server failed! {}".format(e))
            return -1
        try:
            ftp.login(self.username, self.password)
        except Exception as e:
            self.log.error("Login to ftp server failed! {}".format(e))
            return -2
        # 设置缓冲区大小
        bufsize = 4096
        try:
            fp = open(local_file, 'rb')
            ftp.storbinary('STOR %s' % remote_file, fp, bufsize)
        except Exception as e:
            self.log.error("Upload file exception! {}".format(e))
            return -3
        finally:
            fp.close()
            ftp.quit()

        return 0
