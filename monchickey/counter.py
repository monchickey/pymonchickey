# coding=utf-8
import copy
import threading

class Counter(object):
    """python计数器类
    方便嵌在代码中统计数量使用, 提供简单的键值加减取值打印等操作, 默认支持线程安全, 多线程中可以直接使用
    多进程中操作时使用队列相互传递, 执行存取和计数操作时注意加锁
    """
    def __init__(self, count_param=None, is_safe=True):
        """初始化操作
        Args:
            count_param: 初始化起始计数字典 默认为空字典
            is_safe: 是否是线程安全 默认为: True
                线程锁会影响累加效率, 在单线程频繁计数中可以关闭线程安全提高效率
        """
        if count_param is None:
            self.__counts = {}
        else:
            self.__counts = copy.deepcopy(count_param)
        if is_safe:
            self.__is_safe = True
            self.__r_lock = threading.RLock()
        else:
            self.__is_safe = False

    def accumulate(self, key):
        """对key对应的数值进行累加1操作"""
        if self.__is_safe:
            self.__r_lock.acquire()
            self.__accumulate(key)
            self.__r_lock.release()
            return
        self.__accumulate(key)
            

    def __accumulate(self, key):
        """内部执行累加私有方法"""
        if key in self.__counts:
            self.__counts[key] += 1
        else:
            self.__counts[key] = 1

    def decrease(self, key):
        """对key对应的数值进行减1操作
        最后得到的结果可以为负数
        """
        if self.__is_safe:
            self.__r_lock.acquire()
            self.__decrease(key)
            self.__r_lock.release()
            return
        self.__decrease(key)

    def __decrease(self, key):
        """内部执行减1私有方法"""
        if key in self.__counts:
            self.__counts[key] -= 1
        else:
            self.__counts[key] = -1

    def get(self, key):
        """获取计数器key对应的值
        如果key不存在返回0
        """
        if self.__is_safe:
            self.__r_lock.acquire()
            try:
                return self.__get(key)
            finally:
                # print('release.')
                self.__r_lock.release()
        return self.__get(key)

    def __get(self, key):
        """获取计数器key值内部私有方法"""
        if key in self.__counts:
            return self.__counts[key]
        else:
            return 0

    def get_counts(self):
        """获取所有已经统计的结果
        """
        if self.__is_safe:
            self.__r_lock.acquire()
            try:
                return copy.deepcopy(self.__counts)
            finally:
                self.__r_lock.release()
        return copy.deepcopy(self.__counts)

    def print_counts(self):
        """打印所有已经统计的结果"""
        if self.__is_safe:
            self.__r_lock.acquire()
            print(self.__counts)
            self.__r_lock.release()
        else:
            print(self.__counts)
