"""
QUESTION:
Write a function `generate_primes(n)` that generates all prime numbers up to `n` using the Sieve of Eratosthenes algorithm. The function should return a list of prime numbers. The input `n` is a positive integer, and the function should be able to handle large inputs.
"""

def generate_primes(n):
    prime = [True for _ in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    primes = []
    for p in range(2, n + 1):
        if prime[p]:
            primes.append(p)

    return primes