"""
QUESTION:
Write a function `count_primes(n)` that returns the count of all prime numbers from 1 to n (inclusive) where n is a positive integer greater than or equal to 2. Do not use any built-in prime number libraries or functions.
"""

def count_primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1

    count = 0
    for i in range(2, n + 1):
        if is_prime[i]:
            count += 1

    return count