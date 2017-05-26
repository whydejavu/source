#!/usr/bin/python
# _*_ coding:utf-8 _*_

import pandas as pd
import matplotlib.pyplot as plt
# from sklearn.cross_validation import train_test_split

def draw1(data,x,y):
    # 绘制1
    plt.figure(figsize=(4, 4))
    plt.plot(data['TV'], y, 'ro',Label='TV')
    plt.plot(data['Radio'], y, 'g^',Label='Radio')
    plt.plot(data['Newspaper'], y, 'b*',Label='Newspaer')
    plt.legend(loc='lower right')
    plt.grid()
    plt.show()

def draw2(data, x, y):
    # 绘制2
    plt.figure(figsize=(12,4))
    plt.subplot(331)
    plt.plot(data['TV'],y,'ro')
    plt.title('TV')
    plt.grid()
    plt.subplot(332)
    plt.plot(data['Radio'],y,'g^')
    plt.title('Radio')
    plt.grid()
    plt.subplot(333)
    plt.plot(data['Newspaper'],y,'b*')
    plt.title('Newspaper')
    plt.grid()
    plt.tight_layout()
    plt.show()

def pandasxy(data,x,y):
    # 使用 pandas 来构建 X(特征向量)和 y(标签列)
    feature_cols = ['TV','Radio','Newspaper']

    X = data[feature_cols]

    print X.head()

    print type(X)

    print X.shape

    y = data['Sales']

    print y.head()

def trainAndTest():
    pass
    # 构建训练集与测试集
    # X_train,X_test,y_train,y_test = train_test_split(X,y,randon_state=1)

if __name__ =="__main__":
    data = pd.read_csv('resource/Advertising.csv') # Unnamed: 0     TV  Radio  Newspaper  Sales
    print data.head()
    x = data[['TV','Radio','Newspaper']]
    # x = data[['TV','Radio']]
    y = data['Sales']

    draw1(data, x, y)
    draw2(data, x, y)

    pandasxy(data, x, y)
