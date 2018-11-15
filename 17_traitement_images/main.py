#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Manipulation d'images """

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def degrade():
    """ Dégradé diagonal """
    pixels = np.zeros((256, 256, 3), dtype=np.uint8)
    x_range, y_range = np.arange(256), np.arange(256)
    xx, yy = np.meshgrid(x_range, y_range)
    pixels[:, :, 0] = xx
    pixels[:, :, 2] = yy

    return Image.fromarray(pixels)


def disque():
    """ Disque rouge sur fond bleu """
    pixels = np.zeros((256, 256, 3), dtype=np.uint8)
    x_range, y_range = np.arange(256), np.arange(256)
    x, y = np.meshgrid(x_range, y_range)
    masque_interieur = (x[:] - 128)**2 + (y[:] - 128)**2 < 128**2

    pixels[masque_interieur, 0] = 255
    pixels[~masque_interieur, 2] = 255

    return Image.fromarray(pixels)


def niveaux_de_gris(pixels):
    """ Conversion RVB vers niveaux de gris """
    pixels[:, :, :] = 0.2126 * pixels[:, :, 0] + \
    0.7152 * pixels[:, :, 1] + \
    0.0722 * pixels[:, :, 2]
    return pixels


def negatif(pixels):
    """ Négatif """
    pixels[:, :, :] = 255 - pixels[:, :, :]
    return pixels


def floutage(pixels):
    """ Floutage gaussien """
    for _ in range(20):
        pixels[1:-1, 1:-1, :] = 0.25 * pixels[2:, 1:-1, :] + \
                0.25 * pixels[:-2, 1:-1, :] + \
                0.25 * pixels[1:-1, :-2, :] + \
                0.25 * pixels[1:-1, 2:, :]
    return pixels


def slicing(pixels, x_a, y_a, x_b, y_b):
    """ Trace l'intensité le long d'une ligne de pixels """
    pente = (y_b - y_a) / (x_b - x_a)
    if pente > 1:
        raise Exception("Donnez-moi une ligne de pente < à 1 !")
    x = np.arange(pixels.shape[1])
    y = (pente * x + y_a).astype(np.int)
    return np.sum(pixels[x, y, :], axis=1)


def sous_histogramme(pixels):
    """ Calcule l'histogramme d'une image pour une composante """
    hist = np.zeros(256)
    for i in range(256):
        hist[i] = np.sum(pixels == i)

    return hist


def histogramme(pixels):
    """ Calcule l'histogramme d'une image pour chaque composante """
    hist_rouge = sous_histogramme(pixels[:, :, 0])
    hist_vert = sous_histogramme(pixels[:, :, 1])
    hist_bleu = sous_histogramme(pixels[:, :, 2])
    return hist_rouge, hist_vert, hist_bleu


def seuils(hist, percent):
    """ Calcule la classe regroupant :percent: """
    total = hist.shape[0]

    pop = 0.0
    i = 0
    while pop < percent * total:
        pop += hist[i]
        i += 1
    a = i

    pop = 0.0
    i = len(hist) - 1
    while pop < percent * total:
        pop += hist[i]
        i -= 1
    b = i

    return a, b


def augmenter_contraste(pixels, percent):
    """ Étale l'histogramme d'une image """
    for i in range(3):
        hist = sous_histogramme(pixels[:, :, i])
        a, b = seuils(hist, percent)
        a_prime, b_prime = 0, 255
        pixels[:, :, i] = 2 * (b_prime - a_prime) / (b - a) * (
            pixels[:, :, i] - a) + a_prime
    return pixels


def test_dessin():
    """ Test de la génération d'images """
    fig, ax = plt.subplots(1, 2)

    ax[0].imshow(degrade())
    ax[1].imshow(disque())

    plt.show(fig)


def test_traitement():
    """ Test du floutage """
    fig, ax = plt.subplots(1, 2)

    image = Image.open('lena.png')
    pixels = np.asarray(image).copy()

    ax[0].imshow(image)
    ax[1].imshow(Image.fromarray(floutage(pixels)))

    plt.show(fig)


def test_contraste():
    """ Test d'augmentation du contraste """
    fig, ax = plt.subplots(3)

    image = Image.open('ecrevisse.jpg')
    pixels = np.asarray(image).copy()

    pixels_modifies = augmenter_contraste(pixels, 0.1)

    hist_rouge, hist_vert, hist_bleu = histogramme(pixels_modifies)
    ax[0].plot(hist_rouge, color='red')
    ax[1].plot(hist_vert, color='green')
    ax[2].plot(hist_bleu, color='blue')

    fig2 = plt.figure()
    plt.imshow(Image.fromarray(pixels_modifies))

    plt.show()


if __name__ == "__main__":
    test_dessin()
    test_traitement()
    test_contraste()
