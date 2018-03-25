#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np


def LversA(L):
    """Liste de successeurs vers matrice d'adherance"""
    num_sommets = len(L)
    A = np.zeros((num_sommets, num_sommets))
    for i in range(num_sommets):
        for j in range(num_sommets):
            if j in L[i]:
                A[i, j] = 1
    return A


def AversL(A):
    """Matrice d'adherance vers liste de successeurs"""
    num_sommets = A.shape[0]
    L = []
    for i in range(num_sommets):
        L.append([])
    for i in range(num_sommets):
        for j in range(num_sommets):
            if A[i, j]:
                L[i].append(j)
    return L


def degreDeL(L):
    """Renvoie le degre entrant et le degre sortant de chaque sommet"""
    num_sommets = len(L)
    D = np.zeros((num_sommets, 2))
    for i in range(num_sommets):
        # Le degre sortant est le nombre de successeurs
        D[i, 1] = len(L[i])
        degre_entrant = 0
        for j in range(num_sommets):
            if i in L[j]:
                degre_entrant += 1
        D[i, 0] = degre_entrant
    return D


def NbCheminLongueurN(A, i, j, n):
    """Calcule le nombre de chemins de longueur :n: entre :i: et :j:"""
    A_n = A
    for _ in range(n - 1):
        A_n = np.dot(A_n, A)
    return A_n[i, j]


def test_chaine(M, L):
    """Retourne la longueur d'un chemin ou -1 s'il est impossible"""
    depart = L[0]
    longueur_chemin = 0
    for arrivee in L[1:]:
        if M[depart, arrivee] == 0:
            return -1
        longueur_chemin += M[depart, arrivee]
        depart = arrivee
    return longueur_chemin


if __name__ == '__main__':
    A = np.array([[1, 1, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0],
                  [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 0]])
    L = [[0, 1, 3], [2], [3], [4], [5], [1]]

    A_graphe_2 = np.array([
        [1, 1, 0],
        [0, 1, 1],
        [0, 0, 1],
    ])

    print("Question 5")
    print(NbCheminLongueurN(A_graphe_2, 0, 2, 100))

    M = np.array([[0, 1, 3, 2, 4], [1, 0, 9, 0, 8], [3, 9, 0, 7, 0],
                  [2, 0, 7, 0, 0], [4, 8, 0, 0, 0]])
    print(test_chaine(M, [0, 1, 2, 3]))

    # Dijkstra
    L_dijkstra = AversL(M)
    print(L_dijkstra)

    num_sommets = M.shape[0]
    tableau_dijkstra = np.array([float('infinity')] * num_sommets)

    noeud = 0

    while noeud != 4:
        print("Examinons le noeud" + str(noeud))
        for suivant in L_dijkstra[noeud]:
            cout = tableau_dijkstra[noeud] + test_chaine(M, [noeud, suivant])
            if tableau_dijkstra[suivant] == float(
                    'infinity') or cout < tableau_dijkstra[suivant]:
                tableau_dijkstra[suivant] = cout
                noeud = suivant
    print(tableau_dijkstra)
