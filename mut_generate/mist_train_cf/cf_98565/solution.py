"""
QUESTION:
Écrivez une fonction `primes_above_1000()` qui calcule les nombres premiers supérieurs à 1000 tout en excluant les puissances de 2, et renvoie une liste de ces nombres.
"""

import math

def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(n))+1, 2):
            if n % i == 0:
                return False
        return True

def primes_above_1000():
    primes = []
    for n in range(1001, 10000):
        if n % 2 == 0:
            if math.log(n, 2).is_integer():
                continue
        if is_prime(n):
            primes.append(n)
    return primes