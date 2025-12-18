"""
QUESTION:
Write a function `find_prime_seq(arr)` that takes an array of integers `arr` and returns the first permutation of `arr` such that the sum of every pair of neighboring elements is a prime number. If no such permutation exists, the function's behavior is undefined. The input array `arr` contains at least two elements.
"""

import itertools

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if ((n % 2 == 0) or (n % 3 == 0)):
        return False
    i = 5
    while i * i <= n:
        if (n % i == 0) or (n % (i + 2) == 0):
            return False
        i += 6
    return True

def find_prime_seq(arr):
    for perm in itertools.permutations(arr):
        if all(is_prime(perm[i] + perm[i + 1]) for i in range(len(perm) - 1)):
            return perm