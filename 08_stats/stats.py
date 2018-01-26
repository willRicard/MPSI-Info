#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" TD Informatique : Statistiques d'ordre superieur """
import numpy as np


def va_uniforme(taille):
    """ Renvoie une liste de nombres aleatoires de distribution uniforme """
    return list(np.random.randint(0, 10, taille))


def frequences(liste):
    """ Calcule la frequence de chaque valeur dans la liste """
    liste_frequences = [0] * 10
    for valeur in liste:
        liste_frequences[valeur] += 1
    for i, _ in enumerate(liste_frequences):
        liste_frequences[i] /= len(liste)
    return liste_frequences


def moyenne(liste):
    """ Renvoie la moyenne des elements de la liste """
    return sum(liste) / len(liste)


def centrage(liste):
    """ Centre la liste en 0 """
    liste_centree = []
    for i in liste:
        liste_centree.append(i - moyenne(liste))
    return liste_centree


def moment(valeurs, frequences_valeurs, ordre):
    """ Renvoie le moment statistique d'ordre n de la distribution caracterisee par
    :valeurs: et :frequences: """
    moment_distribution = 0
    for valeur in valeurs:
        moment_distribution += valeur**ordre * frequences_valeurs[valeur]
    return moment_distribution


def variance(valeurs, frequences_valeurs):
    """ Renvoie la variance de la liste :valeurs: """
    return moment(valeurs, frequences, 2) - moment(valeurs, frequences_valeurs,
                                                   1)**2


if __name__ == "__main__":
    valeurs_test = range(0, 10)
    liste_test = va_uniforme(100)
    frequences_test = frequences(liste_test)

    print("Frequences:", frequences_test)
    print("Variance:", variance(valeurs_test, frequences_test))

    print("\nCum(X):", moment(valeurs_test, frequences_test, 1))
    print("Cum(X,X):",
          moment(valeurs_test, frequences_test, 2) -
          moment(valeurs_test, frequences_test, 1)**2)
    print("Cum(X,X,X):",
          moment(valeurs_test, frequences_test, 3) -
          3 * moment(valeurs_test, frequences_test, 1) * moment(
              valeurs_test, frequences_test, 2) +
          2 * moment(valeurs_test, frequences_test, 1)**3)
    print("Cum(X,X,X,X):",
          moment(valeurs_test, frequences_test, 4) -
          4 * moment(valeurs_test, frequences_test, 3) * moment(
              valeurs_test, frequences_test, 1) -
          3 * moment(valeurs_test, frequences_test, 2)**2 +
          12 * moment(valeurs_test, frequences_test, 2) * moment(
              valeurs_test, frequences_test, 1)**2 -
          6 * moment(valeurs_test, frequences_test, 1)**4)
