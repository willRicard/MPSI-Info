#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" TD Informatique 10 : Derivation non-entiere, avec des listes """
import matplotlib.pyplot as plt


def fonction_f(x, a, x0):
    """ Renvoie l'image de x par la fonction f """
    if x <= 0:
        return 0
    elif x <= x0:
        return a * x**2
    elif x <= 2 * x0:
        return -a * x**2 + 4 * a * x * x0 - 2 * a * x0**2
    else:
        return 2 * a * x0**2


def derivee_f(liste_x, ordre, pas):
    """ Calcule la derivee n-ieme de f """
    valeurs_derivee = []
    for x in liste_x:
        K = int(x / pas)
        C = [1]
        for k in range(1, K + 1):
            C.append((1 - (ordre + 1) / k) * C[k - 1])
        valeurs_derivee.append((1 / (pas**ordre)) * sum([
            C[k] * fonction_f(pas * (K - k), 1 / (2 * 200**2), 200)
            for k in range(K)
        ]))
    return valeurs_derivee


if __name__ == '__main__':
    x_test = list(range(600))
    y_test = [fonction_f(x, 1 / (2 * 200**2), 200) for x in x_test]
    plt.subplot(2, 1, 1)
    plt.plot(x_test, y_test, label='f')
    plt.subplot(2, 1, 2)
    plt.plot(x_test, derivee_f(x_test, 1.5, 0.1), label='derivee 1.5eme de f')
    plt.legend()
    plt.show()
