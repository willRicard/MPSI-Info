#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Interpolation de points par des spliness de degré 3 """

import matplotlib.pyplot as plt
import numpy as np


def derivee_numerique(x, y):
    """ Approche la dérivée de y par rapport à x. """
    pentes = np.zeros(len(x))
    pentes[0] = (y[1] - y[0]) / (x[1] - x[0])
    pentes[1:-1] = (y[2:] - y[:-2]) / (x[2:] - x[:-2])
    pentes[-1] = (y[-1] - y[-2]) / (x[-1] - x[-2])
    return pentes


def liste_matrices_a(x, y):
    """ Conditions de continuité et de dérivabilité. """

    liste_a = np.zeros((len(x) - 1, 4, 4))
    x_i = x[1:]
    x_i_minus_one = x[:-1]

    # P_i(x_i) = y_i
    liste_a[:, 0, 0] = x_i**3
    liste_a[:, 0, 1] = x_i**2
    liste_a[:, 0, 2] = x_i
    liste_a[:, 0, 3] = 1

    # P_i(x_{i - 1}) = y_{i - 1}
    liste_a[:, 1, 0] = x_i_minus_one**3
    liste_a[:, 1, 1] = x_i_minus_one**2
    liste_a[:, 1, 2] = x_i_minus_one
    liste_a[:, 1, 3] = 1

    # P_i'(x_i) = m_i
    liste_a[:, 2, 0] = 3 * (x_i**2)
    liste_a[:, 2, 1] = 2 * x_i
    liste_a[:, 2, 2] = 1

    # P_i'(x_{i - 1}) = m_{i - 1}
    liste_a[:, 3, 0] = 3 * (x_i_minus_one**2)
    liste_a[:, 3, 1] = 2 * x_i_minus_one
    liste_a[:, 3, 2] = 1

    return liste_a


def liste_matrices_b(x, y):
    """ Conditions de continuité et de dérivabilité - second membre. """

    liste_b = np.zeros((len(x) - 1, 4))

    # P_i(x_i) = y_i
    liste_b[:, 0] = y[1:]
    # P_i(x_{i - 1}) = y_{i - 1}
    liste_b[:, 1] = y[:-1]
    # P_i'(x_i) = m_i
    liste_b[:, 2] = derivee_numerique(x, y)[1:]
    # P_i'(x_{i - 1}) = m_{i - 1}
    liste_b[:, 3] = derivee_numerique(x, y)[:-1]
    return liste_b


def trace_interpolation(x, y):
    """ Trace l'interpolation des points de coordonées (x, y)
    par des splines de degré 3."""

    liste_a, liste_b = liste_matrices_a(x, y), liste_matrices_b(x, y)
    c = np.linalg.solve(liste_a, liste_b)

    x_spline = np.linspace(x[0], x[-1], 200)

    y_spline = np.zeros(len(x_spline))

    for i in range(len(x) - 1):
        mask = (x_spline >= x[i]) & (x_spline <= x[i + 1])
        x_i = x_spline[mask]
        y_spline[mask] = c[i, 0] * (x_i**3) + c[i, 1] * (
            x_i**2) + c[i, 2] * x_i + c[i, 3]

    plt.scatter(x, y)
    plt.plot(x_spline, y_spline)


def main():
    """ Point d'entrée du programme. """

    x_sin = np.linspace(-np.pi, np.pi, 10)
    y_sin = np.sin(x_sin)

    plt.subplot(131)
    plt.title("sin(x)")
    trace_interpolation(x_sin, y_sin)

    x_test = np.array([1, 2, 3, 4, 5])
    y_test = np.array([5, 7, 3, 4, 2])

    plt.subplot(132)
    plt.title("test")
    trace_interpolation(x_test, y_test)

    x_aleatoire = np.linspace(0, 10, 20)
    y_aleatoire = np.random.uniform(size=len(x_aleatoire))

    plt.subplot(133)
    plt.title("Points Aléatoires")
    trace_interpolation(x_aleatoire, y_aleatoire)

    plt.show()


if __name__ == "__main__":
    main()
