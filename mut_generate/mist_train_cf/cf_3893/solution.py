"""
QUESTION:
Create a function `sieve_of_eratosthenes(n)` that efficiently determines whether a given number is prime and prints all the prime numbers between 1 and the given number `n`, where `n` can be up to 10^12. The function should return a list of boolean values representing whether each number is prime or not. Additionally, provide a time complexity analysis for the prime number calculation algorithm used. The function should have a time complexity of O(n log log n).
"""

import math

def sieve_of_eratosthenes(n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False

    for p in range(2, int(math.sqrt(n)) + 1):
        if primes[p] == True:
            for i in range(p*p, n+1, p):
                primes[i] = False

    return primes