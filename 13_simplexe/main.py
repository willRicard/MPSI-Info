#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np


def simplex(conditions):
    """ Optimisation lineaire avec contraintes d'inegalites
    Maximise le gain pour un systeme d'inequations donne

    :conditions: est une matrice dont chaque ligne represente une equation

    """
    while (conditions[-1] > 0).any():
        # Terme contribuant le plus au gain
        colonne_pivot = np.argmax(conditions[-1, :-1])

        # Contrainte la plus forte
        cout = np.zeros(conditions[:-1, colonne_pivot].shape)
        for i, contrainte in enumerate(conditions[:-1, colonne_pivot]):
            if contrainte == 0:
                cout[i] = float('infinity')
            else:
                cout[i] = conditions[i, -1] / conditions[i, colonne_pivot]

        ligne_pivot = np.argmin(cout)
        pivot = (ligne_pivot, colonne_pivot)
        # Normalisation
        conditions[ligne_pivot] /= conditions[pivot]
        for ligne in range(conditions.shape[0]):
            if ligne == ligne_pivot:
                continue
            conditions[ligne] = conditions[ligne]
            -conditions[ligne, colonne_pivot] * conditions[ligne_pivot]
    return conditions


if __name__ == "__main__":
    np.set_printoptions(precision=2, suppress=True)

    test_cours_1 = np.array(
        [[1, 1, 1, 0, 7], [2, 1, 0, 1, 9], [3, 2, 0, 0, 0]], dtype=float)

    test_cours_2 = np.array(
        [[1, 0, 1, 1, 3, 1, 0, 2], [0, 1, 1, 3, 2, 0, 1, 8],
         [100, 100, 500, 900, 1200, 0, 0, 0]],
        dtype=float)

    test_TD = np.array(
        [[3, 2, 1, 0, 0, 1800], [1, 0, 0, 1, 0, 400], [0, 1, 0, 0, 1, 600],
         [30, 50, 0, 0, 0, 0]],
        dtype=float)
    print(simplex(test_cours_1))
    print(simplex(test_cours_2))
    print(simplex(test_TD))
