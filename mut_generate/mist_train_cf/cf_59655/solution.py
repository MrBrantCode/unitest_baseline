"""
QUESTION:
Design a function named `sieve_of_eratosthenes` that takes an integer `n` as input and returns two lists. The first list should contain all prime numbers between 2 and `n` in ascending order, and the second list should contain the same prime numbers in reverse order. The function should be both time-efficient and memory-efficient, with a time complexity of O(n log log n) and a space complexity proportional to the range from 2 to `n`.
"""

def sieve_of_eratosthenes(n):
    primes = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (primes[p] == True):
            for i in range(p * p, n+1, p):
                primes[i] = False
        p += 1

    prime_numbers = [p for p in range(2, n) if primes[p]]
    return prime_numbers, prime_numbers[::-1]