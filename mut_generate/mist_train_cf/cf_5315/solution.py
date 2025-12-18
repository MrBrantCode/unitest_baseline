"""
QUESTION:
Implement the function `sieve_of_eratosthenes(n)` that takes an integer `n` as input and returns a list of all prime numbers below `n`. The function should use the Sieve of Eratosthenes algorithm to optimize its performance.
"""

def sieve_of_eratosthenes(n):
    prime = [True] * (n+1)
    prime[0] = prime[1] = False

    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1

    primes = []
    for p in range(2, n+1):
        if prime[p]:
            primes.append(p)

    return primes