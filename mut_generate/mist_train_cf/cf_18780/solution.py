"""
QUESTION:
Write a function `sum_of_primes(n)` that calculates the sum of all prime numbers smaller than or equal to `n`, where `n` is a positive integer. The function should have a time complexity less than O(n^2) and should not use any external libraries or modules for prime number generation or factorization.
"""

def sum_of_primes(n):
    primes_sum = 0
    for i in range(2, n + 1):
        if all(i % j != 0 for j in range(2, int(i ** 0.5) + 1)):
            primes_sum += i
    return primes_sum