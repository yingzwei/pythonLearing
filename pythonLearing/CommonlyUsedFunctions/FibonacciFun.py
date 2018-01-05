#! D:/Python27/python
# coding=utf-8
import numpy as np
# 只考虑斐波那契数列中取值不超过四百万的项
# 对其中取值为偶数的项进行求和运算

# 计算黄金比例phi
phi = (1 + np.sqrt(5)) / 2

# 2确定取值小于四百万的项的最大索引值
n = np.log(4 * 10 ** 6 * np.sqrt(5) + 0.5) / np.log10(phi)

# 3创建一个从1到n的数组
n = np.arange(1, n)

# 4 计算斐波那契数列
fib = (phi**n - (-1/phi)**n)/np.sqrt(5)

# 5 转换为整数
fib = fib.astype(int)

# 6选出取值为偶数的项
eventerms = fib[fib % 2 == 0]

# 7 对选出的项求和
print(eventerms.sum())
