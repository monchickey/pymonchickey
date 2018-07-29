# coding=utf-8
"""对PyMySQL模块的简单封装
PyMySQL模块同时支持py2和py3
"""
import pymysql

def get_connection(hostname, port, username, password, database, charset='utf8', query_dict=False):
    """获取mysql连接
    Args:
        hostname: 数据库服务器 主机名或ip
        port: 连接数据库服务的端口号 类型为整型
        username: 数据库用户名
        password: 数据库密码
        database: 要连接的数据库
        charset: 连接数据库使用的编码 默认:utf8
        query_dict: 是否开启查询结果以字典形式返回 默认:False 返回tuple类型的结果集
    Returns:
        正常返回数据库连接 注意用完后关闭
        连接异常返回None
    """
    use_cursor_class = pymysql.cursors.Cursor
    try:
        if query_dict:
            use_cursor_class = pymysql.cursors.DictCursor
        connection = pymysql.connect(host=hostname,
                                     port=port,
                                     user=username,
                                     password=password,
                                     db=database,
                                     charset=charset,
                                     cursorclass=use_cursor_class)
        return connection
    except Exception as e:
        return None    # 捕获异常返回None

def close_connection(conn):
    """关闭数据库连接"""
    conn.close()
