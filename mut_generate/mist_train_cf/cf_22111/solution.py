"""
QUESTION:
Create a function called `sum_of_primes(n)` that calculates the sum of all prime numbers up to a given positive integer `n` using the Sieve of Eratosthenes algorithm. The function should not take any input from the user and should only return the sum of prime numbers. The input `n` is a positive integer and the function should not check if the input is valid.
"""

def sum_of_primes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1

    return sum(i for i in range(2, n + 1) if primes[i])