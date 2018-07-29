# coding=utf-8
"""网络工具类"""
import socket

def get_remotehost_ip(hostname):
    """获取远程主机名对应的ip地址, 比如: www.baidu.com"""
    try:
        # 解析主机名为ip地址
        remote_ip = socket.gethostbyname(hostname)
        return remote_ip
    except:
        return None

def socket_http_get(ip, port, uri='/'):
    """使用socket的方式发送简单的get请求 uri必须加/比如 默认不加请求的是/
    此方法只用作测试使用.
    Args:
        ip: 远程服务器主机名或ip
        port: 端口号
        uri: 请求的资源地址, 默认为: '/', 支持参数比如: /user?name=zzy&age=23
    Returns:
        成功: http请求返回所有内容, 如果想确认是否传输成功, 可以通过最后5个跟在html后的字节判断:
            30 0D 0A 0D 0A, 即表示: 0\r\n\r\n, 收到之后则表示内容接收完毕.
        失败: 空字符串, ""
    """
    message = ("GET %s HTTP/1.1\r\n"
               "User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) "
               "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36\r\n"
               "Accept: */*\r\n"
               "Host: %s:%d\r\n"
               "\r\n") % (uri, ip, port)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        s.sendall(message)
        # 获取返回的响应
        bufsize = 4096
        reply = []
        r = s.recv(bufsize)
        while r:
            reply.append(r)
            r = s.recv(bufsize)
        return ''.join(reply)
    except socket.error as errmsg:
        pass
    except Exception as e:
        pass
    finally:
        s.close()
    return ""
