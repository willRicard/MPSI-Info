#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from math import exp

if __name__ == "__main__":
    t = []
    for i in range(1000):
        t.append(i*0.01)
        
    y = [0]
    for i in range(1, 1000):
        y.append(y[i-1] * exp(-0.01/2) + 2.5 * 0.01)
    plt.plot(t, y)
    plt.show()
    
    for i in range(1, 1000):
        y[i] = y[i-1] * (exp(-0.01/5) + exp(-0.01/3)) + (1/5 + 1/3)*0.01
    plt.plot(t, y)
    plt.show()
