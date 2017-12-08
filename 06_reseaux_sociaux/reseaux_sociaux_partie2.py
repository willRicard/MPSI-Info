#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Extrait du concours X-ENS MP Epreuve d'Informatique - Partie 2  """


def question7():
    """ Affiche la représentation des groupes de la figure. """
    parent_a = [5, 1, 1, 3, 4, 5, 1, 5, 5, 7]
    parent_b = [3, 9, 0, 3, 9, 4, 4, 7, 1, 9]
    print("A = ", parent_a, "\n\nB = ", parent_b)


def creerPartitionEnSingletons(taille):
    """ Crée `taille` groupes de 1 élément. """
    parent = [None] * taille
    for i in range(taille):
        parent[i] = i


def representant(parent, i):
    """ Récupère le représentant du groupe de `i`. """
    enfants = []
    while i != parent[i]:
        enfants.append(i)
        i = parent[i]
    for enfant in enfants:
        parent[enfant] = i
    return i


def fusion(parent, i, j):
    """ Fusionne les groupes de `i` et `j`. """
    parent_i = representant(parent, i)
    parent_j = representant(parent, j)
    parent[parent_i] = parent_j


def listeDesGroupes(parent):
    """ Renvoie la partition à partir du tableau des parents. """
    groupes = {}
    for i in range(len(parent)):
        rep = representant(parent, i)
        if rep in groupes:
            groupes[rep].append(i)
        else:
            groupes[rep] = [i]
    liste_groupes = []
    print(groupes)
    for group in groupes:
        liste_groupes.append(group)
    return liste_groupes


if __name__ == "__main__":
    exemple_1 = [5, 1, 1, 3, 4, 5, 1, 5, 5, 7]
    exemple_2 = [3, 9, 0, 3, 9, 4, 4, 7, 1, 9]
    print(listeDesGroupes(exemple_1))
    print(listeDesGroupes(exemple_2))
