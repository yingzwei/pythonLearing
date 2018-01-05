#! D:/Python27/python
# coding=utf-8
__ = 'Administrator'
from datetime import date
import numpy as np
import sys
import tushare as ts

today = date.today()
today1 = str(today)
start = '%s-%s-%s' % (today.year - 1, today.month, today.day)

data = ts.get_hist_data('600567', start=start, end=today1)

close = data['close']

# print close

print ts.inst_detail(retry_count=5, pause=0.001)

print ts.inst_tops()
