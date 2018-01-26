#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt


def derivee(valeurs_x, valeurs_y):
    """ Calcule la derivee de y par rapport a x avec une precision d'ordre 1 """
    valeurs_derivee = (valeurs_y[1:] - valeurs_y[:-1]) / (
        valeurs_x[1:] - valeurs_x[:-1])
    valeurs_derivee = np.append(valeurs_derivee, [valeurs_derivee[-1]])
    return valeurs_derivee


def derivee_ordre2(valeurs_x, valeurs_y):
    """ Calcule la derivee de y par rapport a x avec une precision d'ordre 2 """
    valeurs_derivee = (4 * valeurs_y[1:-1] - valeurs_y[2:] - 3 * valeurs_y[:-2]
                       ) / (valeurs_x[2:] - valeurs_x[:-2])
    valeurs_derivee = np.append(valeurs_derivee, [valeurs_derivee[-1]] * 2)
    return valeurs_derivee


if __name__ == '__main__':
    x = np.arange(0, 10, 0.1)
    y = np.sin(x)
    plt.plot(x, y)
    plt.plot(x, derivee(x, y))
    plt.plot(x, derivee_ordre2(x, y))
    plt.show()
