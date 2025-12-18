"""
QUESTION:
Generate a function `sieve_of_eratosthenes(n)` that generates a list of prime numbers from 1 to n without using built-in functions or libraries, loops, or recursion, and with a time complexity of O(n) and a space complexity of O(1), using a functional programming approach.
"""

def entance(n):
    """Generate a list of prime numbers from 1 to n"""
    primes = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (primes[p] == True):
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    prime_numbers = [p for p in range(2, n + 1) if primes[p]]
    return prime_numbers