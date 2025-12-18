"""
QUESTION:
Implement the function `sieve_of_eratosthenes(n)` that uses the Sieve of Eratosthenes algorithm to find all prime numbers below the given number `n`. The function should return a list of prime numbers. The solution should be optimized for efficiency. The input `n` is a positive integer, and the function should not take any other arguments.
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

    primes = [p for p in range(2, n+1) if prime[p]]
    return primes