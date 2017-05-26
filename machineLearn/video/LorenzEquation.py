#!/usr/bin/python
# _*_ coding:utf-8 _*_

from scipy.integrate import odeint
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def lorenz(state, t):
    print t