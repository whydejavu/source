#!/usr/bin/python
# _*_ coding:utf-8 _*_
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

# 绘制多子图
# 一个Figure对象可以包含多个子图(Axes)，在matplotlib中用Axes对象表示一个绘图区域，在本书中称之为子图。在前面的例子中，Figure对象只包括一个子图。我们可以使用subplot()快速绘制包含多个子图的图表，它的调用形式如下：
# subplot(numRows, numCols, plotNum)
# 图表的整个绘图区域被等分为numRows行和numCols列，然后按照从左到右、从上到下的顺序对每个区域进行编号，左上区域的编号为1。plotNum参数指定所创建Axes对象所在的区域。如果numRows、numCols和plotNum三个参数都小于10，则可以把它们缩写成一个整数，例如subplot(323)和subplot(3,2,3)的含义相同。如果新创建的子图和之前创建的子图区域有重叠的部分，则之前的子图将被删除。

# for idx, color in enumerate("rgbyck"):
#     print idx
#     plt.subplot(321+idx, axisbg=color)
# plt.show()

# plt.subplot(221) # 第一行的左图
# plt.subplot(222) # 第一行的右图
# plt.subplot(212) # 第二整行
# plt.show()

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

plt.figure(1) # 创建图表1
plt.figure(2) # 创建图表2
ax1 = plt.subplot(211) # 在图表2中创建子图1
ax2 = plt.subplot(212) # 在图表2中创建子图2

x = np.linspace(0, 3, 100)
for i in xrange(5):
    plt.figure(1)  # 选择图表1
    plt.plot(x, np.exp(i*x/3))
    plt.sca(ax1)   # 选择图表2的子图1
    plt.plot(x, np.sin(i*x))
    plt.sca(ax2)  # 选择图表2的子图2
    plt.plot(x, np.cos(i*x))

plt.show()

print matplotlib.get_configdir()

