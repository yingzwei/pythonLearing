#! D:/Python27/python
# coding=utf-8
__author__ = 'Administrator'

import numpy as np


N = 600851475143
Lim = 10 ** 6


def factor(n):
    # 1、创建尝试值数组
    a = np.ceil(np.sqrt(n))
    # ceil函数向上取整，如3.21取整后为4
    lim = min(n, Lim)
    a = np.arange(a, a + lim)
    b2 = a ** 2 - n

    # 2、检查数组b2中的元素是否是某个整数的平方
    factions = np.modf(np.sqrt(b2))[0]

    # 3、查找小数部分为0的数组元素
    indices = np.where(factions == 0)
    print indices
    # 4、找到第一
    #
    # 个小数部分为0的数组元素
    print 'take_func:', np.take(a, indices)
    # take：根据数组的下标来取出数组中对应的元素
    # ravel：得到一个展开的一维数组
    a = np.ravel(np.take(a, indices))[0]
    a = int(a)
    print 'ravel_func:', a
    b = np.sqrt(a ** 2 - n)
    b = int(b)
    c = a + b
    d = a - b

    if c == 1 or d == 1:
        return

    print c, d
    factor(c)
    factor(d)


factor(N)