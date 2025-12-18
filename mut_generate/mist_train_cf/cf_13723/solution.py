"""
QUESTION:
Write a function `sieve_of_eratosthenes(n)` that prints all prime numbers in the range 2 to `n`. The function should be able to handle values of `n` up to 10^6.
"""

def entrance(n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False

    p = 2
    while p*p <= n:
        if primes[p]:
            for i in range(p*p, n+1, p):
                primes[i] = False
        p += 1

    result = []
    for i in range(2, n+1):
        if primes[i]:
            result.append(i)
    return result