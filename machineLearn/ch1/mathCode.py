#!/usr/bin/python
# _*_ coding:utf-8 _*_

import pandas as pd
import matplotlib.pyplot as plt
import math
import mpl_toolkits as mpl
import numpy as np

def func(a):
    if a < 1e-6:
        return 0
    last = a
    c = a / 2
    while math.fabs(c - last) > 1e-6:
        last = c
        c = (c + a/c) /2
    return c

if __name__ =="__main__":
    mpl.rcParams['font.sans-serif'] = [u'SimHei']
    mpl.rcParams['axes.unicode_minus'] = False
    x = np.linspace(0,30,num=50)
