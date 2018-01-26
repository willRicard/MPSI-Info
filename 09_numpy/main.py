#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" TD Informatique NumPy """
import numpy as np


def question1():
    """ Creer un vecteur nul de taille 10 """
    return np.zeros(10)


def question2():
    """ Creer un vecteur nul de taille 10 dont le cinquieme element vaut 1 """
    vecteur = np.zeros(10)
    vecteur[4] = 1
    return vecteur


def question3():
    """ Creer un vecteur dont les elements valent de 10 a 49 avec un pas de 1 """
    return np.arange(10, 49, 1)


def question4():
    """ Creer une liste dont les elements valent de 10 a 49 inclus
    avec un pas de 1 puis transformer cette liste en tableau """
    return np.array(range(10, 49))


def question5():
    """ Creer une matrice 3x3 des chiffres de 0 a 8 """
    return np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])


def question6():
    """ Creer une matrice 3x3 des chiffres de 0 a 8 a partir d'un vecteur """
    return np.arange(9).reshape(3, 3)


def question7():
    """ Creer la matrice identite 3x3 """
    return np.eye(3, 3)


def question8():
    """ Creer la matrice diagonale contenant les termes 0, 1, 2, 3 sur la diagonale """
    return np.diag(np.arange(4))


def question9():
    """ Creer la matrice carree conteant les termes 0, 1, 2, 3 juste en dessous de la diagonale """
    return np.diag(np.arange(4), k=-1)


def question10():
    """ Creer une matrice 3x3 de nombres aleatoires """
    return np.random.random((3, 3))


def question11():
    """ Creer un vecteur booleen d'elements True lorsque
    les termes du vecteur [-2, 4, 5, 10, -3, 1] sont positifs et False sinon """
    return np.array([-2, 4, 5, 10, -3, 1]) > 0


def question12():
    """ Creer une matrice 8x8 d'entiers alternant les colonnes 0 et 1 [[0, 1, 0, ...], [0, 1, 0,
    ...], ...]"""
    matrice = np.zeros((8, 8), dtype=int)
    matrice[::, ::2] = 1
    return matrice


def question13():
    """ Creer une matrice 8x8 d'entiers alternant les colonnes 0 et 1 [[0, 1, 0, ...], [1, 0, 1,
    ...], ...] """
    matrice = np.zeros((8, 8), dtype=int)
    matrice[0::2, ::2] = 1
    matrice[1::2, 1::2] = 1
    return matrice


def question14():
    """ Rechercher les valeurs min et max d'une matrice aleatoire 10x10 """
    matrice = np.random.random((10, 10))
    return np.min(matrice), np.max(matrice)


def question15():
    """ Effectuer la multiplication matricielle de A et B"""
    matrice_a = np.array([[2, 3], [3, 10], [9, 20], [10, -1]])
    matrice_b = np.array([[1, 4, 10], [8, 1, 1]])
    return np.dot(matrice_a, matrice_b)


def question16():
    """ Additionner les matrices A et B """
    matrice_a = np.array([[0], [1], [2], [3]])
    matrice_b = np.array([0, 1, 2])
    return matrice_a + matrice_b


def question17():
    """ Creer une matrice 5x5 dont les lignes contiennent les termes de 0 a 4 """
    matrice = np.array([0, 1, 2, 3, 4] * 5)
    return matrice.reshape((5, 5))


def question18():
    """ Trier les termes d'un vecteur aleatoire de taille 10 """
    return np.sort(np.random.random(10))


def question19():
    """ Creer une matrice aleatoire 10x2 puis definir les vecteurs X, Y correspondant
    aux deux colonnes. Calculer la norme des termes de composantes (X[i], Y[i]) """
    matrice = np.random.random((2, 10))
    colonne_x, colonne_y = matrice[0, :], matrice[1, :]
    return np.sqrt(colonne_x**2 + colonne_y**2)


def question20():
    """ Remplacer la valeur maximale d'un vecteur aleatoire de taille 10 par zero """
    vecteur = np.random.random(10)
    vecteur[np.argmax(vecteur)] = 0
    return vecteur


def question21():
    """ Creer un vecteur de 21 termes espaces regulierement de 0 a 2 inclus """
    return np.linspace(0, 2, 21)


def question22():
    """ Taper la commande (...) puis calculer le sinus de x^2+y^2 pour chaque point de la grille """
    tableau_x, tableau_y = np.meshgrid(
        np.arange(-5, 5, 1), np.arange(0, 5, 0.5))
    return np.sin(tableau_x**2 + tableau_y**2)


def question23():
    """ A partir du vecteur a, intercaler trois 0 consecutifs entre chaque terme """
    vecteur = np.arange(1, 5)
    vecteur = vecteur.reshape((4, 1))
    vecteur = np.concatenate((vecteur, np.zeros((4, 3))), axis=1)
    return vecteur.flatten()


def question24():
    """ Concatener verticalement les deux matrices """
    return np.concatenate(
        (
            np.array([[4, 5], [6, 7]]),
            np.array([[10, 20], [30, 40]]),
        ), axis=0)


def question25():
    """ Taper (...) """
    tableau = np.array([[4, 5], [6, 7], [8, 9]])
    return tableau[np.newaxis, :, :]


def question26():
    """ Taper (...) """
    matrice_a = np.array([[4, 5], [6, 7], [8, 9]])
    matrice_b = np.array([[10, 20], [30, 40], [50, 60]])
    matrice_c = np.array([[100, 200], [300, 400], [500, 600]])
    return np.concatenate((matrice_a, matrice_b, matrice_c), axis=1)


if __name__ == '__main__':
    for i, q in enumerate([
            question1, question2, question3, question4, question5, question6,
            question7, question8, question9, question10, question11,
            question12, question13, question14, question15, question16,
            question17, question18, question19, question20, question21,
            question22, question23, question24, question25, question26
    ]):
        print("Question", i + 1, "\n==========\n", q(), "\n")
