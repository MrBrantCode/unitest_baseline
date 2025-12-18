"""
QUESTION:
Write a function called `sieve_of_eratosthenes` that generates an array of prime numbers up to and including the number `n`, where `n` is a positive integer less than or equal to 100. The function should have a time complexity of O(N log log N).
"""

def sieve_of_eratosthenes(n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False

    p = 2
    while p*p <= n:
        if primes[p]:
            for i in range(p*p, n+1, p):
                primes[i] = False
        p += 1

    return [i for i in range(n+1) if primes[i]]