# -*- coding:utf-8 -*-
import random
import hashlib

class DataCompute(object):
    """数据计算类
    用于做一些常用计算, 统计某些信息, 加密算法等
    """
    def text_word_number(self, text, word):
        """统计所给文本中指定某一单词的个数
        """
        num = 0
        while text.find(word) != -1:
            text = text.replace(word, "", 1)
            num = num + 1
        return num

    def text_word_number2(self, text, word):
        """和上述方法功能一样，实现方式不同
        """
        num = 0
        for i in range(0,len(text) - len(word) + 1):
            if text[i:i+len(word)] == word:
                num = num + 1
        return num

    def create_random_number_password(self, number_digits):
        """随机生成指定位数的数字密码
        """
        password = []
        for n in range(0, number_digits):
            password.append(str(random.randint(0, 9)))
        return ''.join(password)

    def generate_md5(self, src):
        """字符串的md5 hash生成
        """
        m = hashlib.md5()
        m.update(src)
        return m.hexdigest()

    def interval_intersection(self, a, b):
        """计算两个区间的交集区间, 默认只处理闭区间
        Args:
            a: 区间1, 类型: list 比如: [3.5, 6.2]
            b: 区间2, 类型: list 比如: [5.8, 7.1]
        Returns:
            返回交集区间元组, 比如上面示例将返回: (5.8, 6.2)
            如果交集不存在, 返回None
            注意: 如果两区间的交集恰好为一个点, 则返回元组的两个元素相等
        """
        if b[0] <= a[1] and a[0] <= b[1]:
            left_number = max(a[0], b[0])
            right_number = min(a[1], b[1])
            return left_number, right_number
        return None

    def get_function_zero(self, func, interval, accuracy):
        """计算函数的零点, 即一元方程f(x) = 0的近似解
        依据和方法: 零点定理和二分法
        Args: 
            func: 函数本身, 类型: python函数, 可以直接被调用, 相当于f(x), 传入x返回函数值
            interval: 零点所在区间, 类型: 元组 假设为: (3, 6) 则首先保证: f(3) * f(6) < 0
            accuracy: 精度, 当区间范围缩小至|a - b| < accuracy时, 即返回求解结果
        Returns:
            计算成功返回方程f(x) = 0的一个解
            计算未得到结果返回: None
        """
        a = interval[0]
        b = interval[1]
        ya = func(a)
        yb = func(b)
        if ya * yb > 0:
            return None
        if ya == 0:
            return a
        if yb == 0:
            return b
        num = 0
        while True:
            c = (a + b)/2.0
            yc = func(c)
            if yc == 0:
                return c
            elif ya * yc < 0:
                b = c
                yb = yc
            elif yc * yb < 0:
                a = c
                ya = yc
            num += 1
            if abs(a - b) < accuracy:
                # print('num: %d' % num)
                return a
