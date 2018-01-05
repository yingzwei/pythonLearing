# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

''' 
# plot 基础
x = np.linspace(-3, 3, 50)
y1 = 2*x+1
y2 = x**2

plt.plot(x, y1)
plt.plot(x, y2, color ='red', linestyle = '--', linewidth =1.0 )
plt.show()
'''
x = np.linspace(-3, 3, 50)
y1 = 2 * x + 1
y2 = x ** 2

plt.plot(x, y1)
plt.plot(x, y2, color='red', linestyle='--', linewidth=1.0)
plt.xlim(-2, 2)
plt.ylim(-3, 3)

plt.xlabel(r'x axis')
plt.ylabel(r'y axis')

new_ticks = np.linspace(-2, 2, 5)
plt.xticks(new_ticks)
plt.xticks([-3, -1, 1, 2, 3]
           , [r'$real\ bad$', r'$bad$', r'$\alpha$', r'$good$'r'$real\ good$'])

plt.show()
