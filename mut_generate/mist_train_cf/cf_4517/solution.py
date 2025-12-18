"""
QUESTION:
Write a function called lowest_integer_not_sum_of_three_primes that finds the lowest positive integer that cannot be represented as the sum of exactly three distinct prime numbers, where the sum of the three primes is the largest possible prime number less than or equal to the given positive integer. The function should have a time complexity of O(n^2) or better.
"""

def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1

    return [i for i in range(n + 1) if primes[i]]


def lowest_integer_not_sum_of_three_primes(n):
    primes = sieve_of_eratosthenes(n)
    
    for num in range(2, n):
        if not any(num - prime in primes for prime in primes):
            return num

    return -1  # If no such number exists