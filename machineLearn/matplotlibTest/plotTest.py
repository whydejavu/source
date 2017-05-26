#!/usr/bin/python
# _*_ coding:utf-8 _*_

import numpy as np
import matplotlib.pyplot as plt
from StringIO import StringIO
# import numpy as np
# import matplotlib.pyplot as plt
plt.figure(1) # 创建图表1
plt.figure(2) # 创建图表2
ax1 = plt.subplot(211) # 在图表2中创建子图1
ax2 = plt.subplot(212) # 在图表2中创建子图2
x = np.linspace(0, 3, 100)
for i in xrange(5):
    plt.figure(1)  #❶ # 选择图表1
    plt.plot(x, np.exp(i*x/3))
    plt.sca(ax1)   #❷ # 选择图表2的子图1
    plt.plot(x, np.sin(i*x))
    plt.sca(ax2)  # 选择图表2的子图2
    plt.plot(x, np.cos(i*x))
plt.show()


# 坐标轴的显示值
x = np.linspace(0, 10, 1000)
y = np.sin(x)
z = np.cos(x**2)

plt.figure(figsize=(8,4))
print plt.rcParams["savefig.dpi"]

# label：给曲线指定一个标签名称，此标签将在图示中显示。如果标签字符串的前后有字符’$’，则matplotlib会使用其内嵌的LaTex引擎将其显示为数学公式。
# color：指定曲线的颜色，颜色可以用英文单词，或者以’#’字符开头的三个16进制数，例如’#ff0000’表示红色。或者使用值在0到1范围之内的三个元素的元组表示，例如(1.0, 0.0, 0.0)也表示红色。
# linewidth：指定曲线的宽度，可以不是整数，也可以使用缩写形式的参数名lw。
# plt.plot(x,y,label="$sin(x)$",color="red",linewidth=2)
# plt.plot(x,z,"b--",label="$cos(x^2)$")

# 设置x轴文字
plt.xlabel("Time(s)")
# 设置y轴文字
plt.ylabel("Volt")
# 设置标题
plt.title("PyPlot First Example")
# 设置y轴显示范围
plt.ylim(-10.2,50.2)
# 显示图示，即图中表示每条曲线的标签(label)和样式的矩形区域。
plt.legend()

# 这两个方法一个是显示到屏幕，一个事输出到文件
# plt.show()
# plt.savefig("test.png", dpi=120)

# buf = StringIO() # 创建一个用来保存图像内容的StringIO对象
# plt.savefig(buf, fmt="png") # 将图像以png格式保存进buf中
# print buf.getvalue()[:20] # 显示图像内容的前20个字节

# fig = plt.gcf()
# axes = plt.gca()
# print fig
# print axes

# 配置属性
# matplotlib所绘制的图表的每个组成部分都和一个对象对应，我们可以通过调用这些对象的属性设置方法set_*()或者pyplot模块的属性设置函数setp()设置它们的属性值。例如plot()返回一个元素类型为Line2D的列表，下面的例子设置Line2D对象的属性：
x = np.arange(0,5,0.1)
line = plt.plot(x, x*x)[0] # plot返回一个列表
line.set_antialiased(False) # 调用Line2D对象的set_*()方法设置属性值
lines = plt.plot(x, np.sin(x), x, np.cos(x))
plt.setp(lines, color="r", linewidth=2.0)

plt.show()