#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Travaux Pratiques d'Informatique : SÃ©quences """

from random import randint
from math import sqrt


def max_liste(liste):
    """max_liste renvoie un tuple contenant le plus grand Ã©lÃ©ment d'une liste et son index."""
    maximum = 0
    indice = 0
    for i, element in enumerate(liste):
        if element > maximum:
            maximum = element
            indice = i
    return maximum, indice


def liste_hasard(longueur, borne_sup):
    """ renvoie une liste de nombres alÃ©atoires """
    liste = [0] * longueur
    for i in range(longueur):
        liste[i] = randint(0, borne_sup)
    return liste


def moyenne(liste):
    """ renvoie la moyenne des valeurs d'une liste """
    return sum(liste) / len(liste)


def ecart_type(liste):
    """ecart_type renvoie l'Ã©cart-type des nombres d'une liste."""
    somme = 0
    moyenne_liste = moyenne(liste)
    for element in liste:
        somme += (moyenne_liste - element)**2
    return sqrt(somme / (len(liste) - 1))


def stat_liste(liste):
    """stat_liste renvoie un tuple contenant la moyenne et l'Ã©cart-type des nombres d'une liste."""
    return moyenne(liste), ecart_type(liste)


if __name__ == "__main__":
    liste_test = liste_hasard(100, 20)
    print(liste_test)
    print("Moyenne: %f\nÃ‰cart-type: %f" % stat_liste(liste_test))
