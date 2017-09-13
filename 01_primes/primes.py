#!/usr/bin/env python3
from math import sqrt


def is_prime(n, primes=None):
    if primes is not None:
        for p in primes:
            if n % p == 0:
                return False
            elif p > sqrt(n):
                return True
    else:
        for p in range(2, n):
            if n % p == 0:
                return False
            elif n > sqrt(n):
                return True
        return n != 1


def next_prime(n, primes=None):
    m = n + 1
    while not is_prime(m, primes):
        m = m + 1
    return m


if __name__ == "__main__":
    primes = [2]
    while len(primes) < 100:
        primes.append(next_prime(primes[-1]))
    print(primes)
