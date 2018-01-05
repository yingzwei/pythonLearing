#! D:/Python27/python
# coding=utf-8
__author__ = 'Administrator'

import numpy as np
import numpy.testing as testing

# 回文数从左或是从右读都是一样的 1001001
a = np.arange(100, 1000)
testing.assert_equal(100, a[0])
testing.assert_equal(999, a[-1])

numbers = np.outer(a, a)
numbers = np.ravel(numbers)
numbers.sort()
testing.assert_equal(810000, len(numbers))
testing.assert_equal(10000, numbers[0])
testing.assert_equal(998001, numbers[-1])

for i in xrange(-1, -1 * len(numbers), -1):
    s = str(numbers[i])
    if s == s[::-1]:
        print s
        break