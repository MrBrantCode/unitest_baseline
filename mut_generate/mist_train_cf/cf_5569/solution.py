"""
QUESTION:
Write a function `sieve_of_eratosthenes(n)` that implements the Sieve of Eratosthenes algorithm to generate a boolean array where `prime[i]` is `True` if `i` is prime and `False` otherwise. The function should be able to efficiently handle prime numbers up to 10^6.
"""

def sieve_of_eratosthenes(n):
    prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if prime[p] == True:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    return prime