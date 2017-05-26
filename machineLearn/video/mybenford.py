# -*- coding:utf-8 -*-
# /usr/bin/python

from itertools import imap
import numpy as np
from time import time
import matplotlib.pyplot as plt

# 本福特定律

# 一般阶乘算法
# 方法1
def factorial1(n):
    assert n >= 0
    if n < 2:
        return 1
    else:
        return n * factorial1(n-1)
# 方法2
def factorial2(n):
    return reduce(lambda x, y: x * y, [1] + range(1, n + 1))
# 方法3
def factorial3(x):
    result = 1
    for i in xrange(2, x + 1):
        result *= i
    return result
# 方法4
def factorial4(x):
    return reduce(long.__mul__, imap(long, xrange(1, x + 1)))

# 方法5 阶乘求法，数学简化
def myfactorial(n):
    x = range(1, n + 1)
    # print np.log10(x)
    # y = sum(np.log10(x))
    # print y
    # print sum(y)
    number = np.sum(np.log10(x)) #np.sum 和sum 时间上是不同的，会差一倍
    # number = sum(np.log10(x))
    print "number:",number
    print "int(number):",int(number)
    number -= int(number)     ##这里将756570556.209 去除整数 使用小数 0.208761572838
    print "number:", number
    # 10 ** sum(y)
    print "myfactorial结果：",10**number
    # return 10**number
def teachfactorial(n):
    x = range(1, n + 1)
    # print x
    # print "np log x:",np.log10(x)
    y = np.cumsum(np.log10(x))
    # print "np cumsum y:",y
    number = y[n-1]
    print "number:", number
    print "int(number):", int(number)
    number -= int(number)
    print "number:", number
    # map(num,y)
    print "teachfactorial结果：",10**number

# 暂时使用np的log10
def mylog10(x1):
    return np.log10(x1)

# 阶乘测试
def factorialtest(n):
    # print n,"的阶乘：",myfact(n)
    # print "首位：",str(myfact(n))[0]
    # firstnum = int(str(myfact(n))[0])

    # print n,"的阶乘：",factorial2(n)
    # print "首位：",str(factorial2(n))[0]
    # firstnum = int(str(factorial2(n))[0])

    # print n,"的阶乘：",factorial3(n)
    # print "首位：",str(factorial3(n))[0]
    # firstnum = int(str(factorial3(n))[0])

    print n,"的阶乘：",factorial4(n)
    print "首位：",str(factorial4(n))[0]
    firstnum = int(str(factorial4(n))[0])

    firstnum = firstnum-1
    # frequency[firstnum] =  frequency[firstnum]+1
    # print factorial2(n)
    # print factorial3(n)
    # print factorial4(n)

# 首位 任意长度数值的首位
def funfirstnum(num):
    firstnum = int(str(num)[0])
    print "首位：", firstnum
    return firstnum

def num(number):
    number -= int(number)
    # print "10 ** ",number,":",int(10 ** number)

def top4(number):
    number -= int(number)
    frequency[int(10 ** number) - 1] += 1

if __name__ == '__main__':
    N = 1000000                #常数，表示求1-N的阶乘
    x = range(1, N + 1)     #生成1-N数组
    # print x
    # factorialtest(3)        #测试阶乘方法
    frequency = np.zeros(9, dtype=np.int)
    # # print frequency
    # print '开始计算...'
    # t0 = time()
    # map(factorialtest,x)    #此方法将x数组中的数据一项一项的在factorialtest方法中运行
    # t1 = time()
    # print '耗时：', t1 - t0
    # print frequency
    # plt.figure(facecolor='w')
    # t = np.arange(1, 10)
    # plt.plot(t, frequency, 'r-', t, frequency, 'go', lw=2, markersize=8)
    # for x,y in enumerate(frequency):
    #     plt.text(x+1.1, y, frequency[x], verticalalignment='top', fontsize=15)
    # plt.title(u'%d!首位数字出现频率' % N, fontsize=18)
    # plt.xlim(0.5, 9.5)
    # plt.ylim(0, max(frequency)*1.03)
    # plt.grid(b=True)
    # plt.show()

    print x
    print "np log x:",np.log10(x)
    y = np.cumsum(np.log10(x))
    print "np cumsum y:",y
    map(top4,y)
    print y
    print frequency
    plt.figure(facecolor='w')
    t = np.arange(1, 10)
    plt.plot(t, frequency, 'r-', t, frequency, 'go', lw=2, markersize=8)
    for x, y in enumerate(frequency):
        plt.text(x + 1.1, y, frequency[x], verticalalignment='top', fontsize=15)
    plt.title(u'%d!首位数字出现频率' % N, fontsize=18)
    plt.xlim(0.5, 9.5)
    plt.ylim(0, max(frequency) * 1.03)
    plt.grid(b=True)
    plt.show()

    print N,'阶乘开始计算...'
    print format(N)
    jt0 = time()
    myfactorial(N)
    # print "myfactorial结果：",myfactorial(N)
    jt1 = time()
    print 'myfactorial耗时：', jt1 - jt0
    # # factorial2(N)
    # jt2 = time()
    # print 'factorial2耗时：', jt2 - jt1
    teachfactorial(N)
    jt3 = time()
    print 'teachfactorial耗时：', jt3 - jt1


