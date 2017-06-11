# coding=utf-8
import socket

class NetworkTools(object):
    """网络工具类"""

    # 获取指定远程主机名对应的ip地址,不加http:// 比如:help.baidu.com
    def get_remotehost_ip(self, hostname):
        try:
            # 解析主机名为ip地址
            remote_ip = socket.gethostbyname(hostname)
            return remote_ip
        except Exception, e:
            print e
            print "host解析失败..."
            return ""

    # 向指定的ip和端口以socket方式发送get请求 uri必须加/比如/life?name=sc&sq=09 默认不加请求的是/
    def use_socket_send_request(self, ip, port, uri):
        message = "GET %sHTTP/1.1 \r\n\r\n" % uri
        # print message
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            s.sendall(message)
            # 获取返回的响应
            r = s.recv(4096)
            reply = r
            r = s.recv(4096)
            # 如果返回内容多 则分批获取
            while len(r) > 0:
                reply = reply + r
                r = s.recv(4096)
                # print "read..."
            return reply
        except socket.error, msg:
            print msg[1]
            print "socket error..."
            return ""
        except Exception, e:
            print e
            print "error.."
            return ""
        finally:
            print "close socket..."
            s.close()
        