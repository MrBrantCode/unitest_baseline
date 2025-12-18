"""
QUESTION:
Write a function `sum_of_primes(n)` that calculates the sum of all prime numbers between 1 and `n`. The function should return the total sum of prime numbers in the given range. The input `n` is a positive integer.
"""

def sum_of_primes(n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False
    p = 2
    prime_sum = 0

    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n+1, p):
                primes[i] = False
        p += 1

    for i in range(2, n+1):
        if primes[i]:
            prime_sum += i

    return prime_sum