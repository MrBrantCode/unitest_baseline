"""
QUESTION:
Implement a function `sieve_of_eratosthenes` to generate prime numbers up to a given limit `n` using the Sieve of Eratosthenes algorithm, and another function `generate_primes` to return a list of prime numbers. The functions should be designed to handle prime numbers up to 10^6 efficiently.
"""

def sieve_of_eratosthenes(n):
    prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if prime[p] == True:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    primes = []
    for p in range(2, n + 1):
        if prime[p]:
            primes.append(p)
    return primes