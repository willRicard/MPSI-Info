#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Calculs d'optique """


def distance_focale(ior, radius):
    """ Renvoie la distance focale d'une lentille
    mince d'indice de réfraction n et de rayon de courbure R. """
    return radius / (ior - 1)


if __name__ == "__main__":
    print("Indice de réfraction de la lentille")
    n = float(input())
    print("Rayon de courbure:")
    r = float(input())
    print(distance_focale(n, r))
