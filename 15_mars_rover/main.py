#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

from random import random, randint, shuffle
from copy import deepcopy


def position_robot():
    """ Retourne la position du robot sur la grille """
    return 5, 5


def generer_PI(n, cmax):
    """ Genere :n: points d'interet sur une grille carree de taille :cmax: """
    PI = []
    while (len(PI) < n):
        pos_x = randint(0, cmax)
        pos_y = randint(0, cmax)
        pos = [[pos_x, pos_y]]
        if pos not in PI:
            PI += pos
    return np.array(PI)


def afficher_PI(PI, ax):
    """ Affichage des points d'interet """
    ax.scatter(PI[:, 0], PI[:, 1])


def calculer_distances(PI):
    """ Calcule la distance entre chaque couple de points (points d'interet et position du robot) """
    x, y = position_robot()
    NPI = np.concatenate((PI, np.array([[x, y]])))
    n = len(NPI)
    poH = NPI.reshape((1, n, 2))
    poV = NPI.reshape((n, 1, 2))
    return np.sqrt((poH[:, :, 0] - poV[:, :, 0])**2 +
                   (poH[:, :, 1] - poV[:, :, 1])**2)


def longueur_chemin(chemin, distances):
    """ Calcule la longueur d'un chemin """
    n = len(distances) - 1
    return distances[chemin, [n] + chemin[:-1]].sum()


def normaliser_chemin(chemin, n):
    """ Supprime les doublons et rajoutes les noeuds manquants a un chemin """
    for noeud in chemin:
        i = chemin.index(noeud)
        if noeud in chemin[i + 1:]:
            chemin.remove(noeud)
    for i in range(n):
        if i not in chemin:
            chemin.append(i)
    return chemin


def afficher_chemin(PI, chemin, ax, **kwargs):
    """ Affichage d'un chemin """
    x, y = [], []
    for noeud in chemin:
        if noeud < len(chemin) - 1:
            x.append(PI[noeud, 0])
            y.append(PI[noeud, 1])
        else:
            x_robot, y_robot = position_robot()
            x.append(x_robot)
            y.append(y_robot)
    ax.add_line(Line2D(x, y, **kwargs))


def creer_population(n, distances):
    """ Cree :n: chemins aleatoires """
    num_points = len(distances)
    population = []
    chemin = list(range(num_points))
    for i in range(n):
        shuffle(chemin)
        population.append(chemin)
    return population


def reduire(population, distances):
    """ Reduit la population en conservant seulement les meilleurs chemins """
    n = len(population)
    longueurs = []
    for i in range(n):
        longueurs.append(longueur_chemin(population[i], distances))

    longueurs_triees = deepcopy(longueurs)
    longueurs_triees.sort()
    longueur_limite = longueurs_triees[int(-n / 2)]

    next_population = []
    for i, chemin in enumerate(population):
        if len(next_population) > int(len(population) / 2):
            break
        if longueurs[i] <= longueur_limite:
            next_population.append(chemin)
    return next_population


def muter_chemin(chemin):
    """ Echange deux noeuds au hasard """
    i = randint(0, len(chemin) - 2)
    chemin[i], chemin[i + 1] = chemin[i + 1], chemin[i]


def muter_population(population, proba):
    """ Mute chaque chemin """
    for i, chemin in enumerate(population):
        if random() < proba:
            muter_chemin(chemin)


def croiser(c1, c2):
    """ Combine deux chemins """
    midpoint = int(len(c1) / 2)
    return c1[0:midpoint] + c2[midpoint:]


def nouvelle_generation(p, d):
    """ Cree une nouvelle population en combinant les meilleurs chemins """
    population = []
    for i in range(len(p)):
        population.append(croiser(p[i][0], p[i][1]))
    return population


def algo_genetique(PI, m, proba, g):
    """ Algorithme genetique 
    :m: taille de la population
    :proba: taux de mutation
    :g: nombre de generations
    """
    distances = calculer_distances(PI)
    population = creer_population(m, distances)
    for generation_id in range(g):
        population = reduire(population, distances)

        parents = []
        for i in range(len(population) - 1):
            parents.append((population[i], population[i + 1]))
        parents.append((population[-1], population[0]))

        population.extend(nouvelle_generation(parents, distances))
        muter_population(population, proba)
        for chemin in population:
            normaliser_chemin(chemin, len(distances))
    longueurs = []
    for chemin in population:
        longueurs.append(longueur_chemin(chemin, distances))
    return population[longueurs.index(min(longueurs))]


def voyageur_de_commerce(PI, d):
    """ Algorithme de Held-Karp """
    from itertools import combinations
    n = len(d)
    C = {}
    for k in range(1, n):
        C[(1 << k, k)] = (d[0][k], 0)
    for subset_size in range(2, n):
        for subset in combinations(range(1, n), subset_size):
            bits = 0
            for bit in subset:
                bits |= 1 << bit
            for k in subset:
                prev = bits & ~(1 << k)
                res = []
                for m in subset:
                    if m == 0 or m == k:
                        continue
                    res.append((C[(prev, m)][0] + d[m][k], m))
                C[(bits, k)] = min(res)
    bits = (2**n - 1) - 1
    res = []
    for k in range(1, n):
        res.append((C[(bits, k)][0] + d[k][0], k))
    opt, parent = min(res)
    path = []
    for i in range(n - 1):
        path.append(parent)
        new_bits = bits & ~(1 << parent)
        _, parent = C[(bits, parent)]
        bits = new_bits
    path.append(0)
    return opt, list(reversed(path))


if __name__ == "__main__":
    ax_genetique = plt.subplot(2, 1, 1)
    ax_held_karp = plt.subplot(2, 1, 2)

    ax_genetique.set_title("Algorithme Genetique")
    ax_held_karp.set_title("Held-Karp")

    PI = generer_PI(10, 100)
    d = calculer_distances(PI)

    afficher_PI(PI, ax_genetique)
    afficher_PI(PI, ax_held_karp)

    chemin = algo_genetique(PI, 100, 0.01, 100)
    afficher_chemin(PI, chemin, ax_genetique, linewidth=2, color='red')

    test_cout, test_chemin = voyageur_de_commerce(PI, d)
    afficher_chemin(PI, test_chemin, ax_held_karp, linewidth=2, color='lime')

    plt.tight_layout()
    plt.show()
