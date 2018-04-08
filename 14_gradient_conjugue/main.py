#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from fractions import Fraction

np.set_printoptions(formatter={
    'all': lambda x: str(Fraction(x).limit_denominator())
})


def gradient_conjugue(A, b):
    N = A.shape[0]
    x = np.zeros((N, 1))
    p = np.zeros((N, N, 1))
    for i in range(N):
        r = b - A.dot(x)

        S = np.zeros((N, 1))
        for j in range(i):
            S += ((p[j].T.dot(A).dot(r)) / (p[j].T.dot(A).dot(p[j]))) * p[j]

        p[i] = r - S

        alpha = (p[i].T.dot(b)) / (p[i].T.dot(A).dot(p[i]))

        x += alpha * p[i]
    return x


if __name__ == "__main__":
    test_cours_A = np.array([[4, 1], [1, 3]])
    test_cours_b = np.array([[1], [2]])
    print(np.linalg.inv(test_cours_A) * test_cours_b)

    test_TD_A = np.array([[4, 1, 0], [1, 2, 1], [0, 1, 3]])
    test_TD_b = np.array([[1], [2], [1]])

    print(gradient_conjugue(test_cours_A, test_cours_b))
    print(gradient_conjugue(test_TD_A, test_TD_b))
