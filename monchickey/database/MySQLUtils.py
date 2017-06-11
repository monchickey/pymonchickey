# coding=utf-8
import MySQLdb
'''
mysql操作工具类
'''
class MySQLUtils(object):

    # 获取mysql连接 (关于游标和设置编码在外部调用时适当封装执行, 单一游标移动更高效)
    def get_connection(self, hostname, port, username, password, db_name, charset='utf8'):
        try:
            db = MySQLdb.connect(host=hostname,
                    port=port,
                    user=username,
                    passwd=password,
                    db=db_name,
                    charset=charset)
            return db
        except Exception, e:
            return None
        # self.conn = self.db.cursor()
        # self.conn.execute("SET NAMES utf8")

    # 获取sql执行结果 查询不到结果返回-1  默认返回列表和元组类型的数据 必须通过序号获得
    def get_sql_result(self, cursor, sql):
        cursor.execute(sql)
        results = cursor.fetchall()
        if results != None and len(results) > 0:
            return results
        else:
            return -1

    # 获取sql执行结果 查询不到结果返回-1  默认返回字典list集合 直接通过字段名获得即可方便
    def get_select_result(self, cursor, sql):
        cursor.execute(sql)
        rs = cursor.fetchall()
        results = []
        if rs != None and len(rs) > 0:
            for row in rs:
                temp = {}
                i = 0
                for desc in cursor.description:
                    temp[desc[0]] = row[i]
                    i = i + 1
                results.append(temp)
            return results
        else:
            return -1

    # 向数据库插入记录 (同时适用于更新或删除记录)
    def insert_record(self, db_conn, sql):
        try:
            cursor = db_conn.cursor()
            cursor.execute(sql)
            db_conn.commit()
            return 0
        except:
            # 发生异常回滚
            db_conn.rollback()
            return -1

    # 关闭连接
    def close(self, db_conn):
        db_conn.close()
        