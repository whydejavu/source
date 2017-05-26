#!/usr/bin/python
# _*_ coding:utf-8 _*_

from matplotlib.font_manager import fontManager
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
import numpy as np
import os
import os.path

fig = plt.figure(figsize=(12,6))
ax = fig.add_subplot(111)
plt.subplots_adjust(0, 0, 1, 1, 0, 0)
plt.xticks([])
plt.yticks([])
x, y = 0.05, 0.08
fonts = [font.name for font in fontManager.ttflist if
    os.path.exists(font.fname) and os.stat(font.fname).st_size>1e6]
font = set(fonts)
dy = (1.0-y)/(len(fonts)/4 + (len(fonts)%4!=0))
for font in fonts:
    print font
    t = ax.text(x, y, u"中文字体", {'fontname':font, 'fontsize':14}, transform=ax.transAxes)
    ax.text(x, y-dy/2, font, transform=ax.transAxes)
    x += 0.25
    if x >= 1.0:
        y += dy
        x = 0.05
plt.show()

# font = FontProperties(fname=r"Trattatello", size=14)
t = np.linspace(0, 10, 1000)
y = np.sin(t)
font = "Trattatello"
plt.plot(t, y)
plt.xlabel(u"时间", fontproperties=font)
plt.ylabel(u"振幅", fontproperties=font)
plt.title(u"正弦波", fontproperties=font)
plt.show()