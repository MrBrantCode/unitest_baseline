"""
QUESTION:
Write a function `sieve_of_eratosthenes` to generate a boolean list representing prime numbers up to a given number `n` using the Sieve of Eratosthenes algorithm. The function should have a time complexity of O(n log(log n)) and return a list where the index represents the number and the value at that index is True if the number is prime, False otherwise.
"""

import math

def sieve_of_eratosthenes(n):
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False

    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    return prime