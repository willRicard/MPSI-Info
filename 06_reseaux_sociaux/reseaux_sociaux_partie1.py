#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Extrait du concours X-ENS MP Épreuve d'Informatique  """


def question1():
    """ Affiche les représentations des réseaux de la figure. """
    reseau_a = [5, [[0, 1], [0, 1], [0, 2], [0, 3], [1, 2], [2, 3]]]
    reseau_b = [5, [[0, 1], [1, 2], [2, 4], [2, 3], [4, 3], [3, 1]]]
    print("A = ", reseau_a, "\n\nB = ", reseau_b)


def creerReseauVide(taille):
    """ Renvoie un réseau vide de `taille` nœuds. """
    return [taille, []]


def estUnLienEntre(paire, i, j):
    """ Renvoie True si `paire` est un lien entre `i` et `j`. """
    return (i in paire) and (j in paire)


def sontAmis(reseau, i, j):
    """ Parcourt le réseau et renvoie True si `i` et `j` sont amis. """
    for lien in reseau[1]:
        if estUnLienEntre(lien, i, j):
            return True
    return False


def declareAmis(reseau, i, j):
    """ La complexité de cette fonction est en O(m), m nombres d'arêtes """
    if sontAmis(reseau, i, j):
        return
    else:
        reseau[1].append([i, j])


def listeDesAmisDe(reseau, i):
    """ La complexité de cette fonction est en O(n), n nombre de personnes. """
    amis = []
    for j in range(reseau[0]):
        if sontAmis(reseau, i, j):
            amis.append(j)
    return amis


if __name__ == "__main__":
    question1()
