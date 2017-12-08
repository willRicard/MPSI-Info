#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Une série de tests qui mettent en évidence l'architecture des listes. """

def q1():
    l1, l2 = [[2, 3], [4], 10], [[[11]]]
    l3 = l1 + l2
    l1.extend(l2)
    l4 = l1
    print(l3)
    print(l4)
    l3[3][0] = 5
    l1[1][0] = 8
    l1[2] = [10]
    print(l1)


def q2():
    l2 = [10, [3, 4], 2]
    l0 = l2 * 4
    print(l0[1::3])


def q3():
    l5 = ((1, 2), (10, 20))
    l6 = (100, 200)
    l7 = l5 + l6
    l8 = ([2, 3], 4, 5)
    l8[0][0] = 20
    print(l8)


def q4():
    l10 = "abc12"
    l11 = list(l10 * 2)
    print(l11[2:20:3])


def q5():
    print("-00".join("abcde"))
    l20 = "tant que la condition".split()
    print(l20)


def q6():
    a = b = c = d = [20, 21]
    b = 3
    c = 10
    a[1] = 4
    print(a, b, c, d)


def q7():
    l12 = list(range(2, 20, 3))
    print(l12)
    print(l12[-2:1:-1])


def q8():
    print("o" in "coeur")
    print("o" + "e" in "coeur")
    print("oe" in "coeur")


def q9():
    l13 = [[1, 3], 2, 4]
    l13[2] = [23, 24]
    print(l13)
    l13[1:3] = [0]
    print(l13)


def q10():
    a, b, c = 2, 3, [4, 5]

    def f():
        b, c = 20, 3
        print(a, b, c)

    f()
    print(a, b, c)


def q11():
    a, b, c = 2, 3, [4, 5]

    def f():
        b, c[0] = 20, 3
        return b, c

    print(a, b, c)
    print(f())
    print(a, b, c)


if __name__ == "__main__":
    tests = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11]
    for i, test in enumerate(tests):
        print("Question #" + str(i + 1) + "\n----------------\n")
        tests[i]()
        print("\n")
