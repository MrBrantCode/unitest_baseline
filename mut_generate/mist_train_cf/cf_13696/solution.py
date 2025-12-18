"""
QUESTION:
Write a function named `count_primes` that takes an integer `n` greater than or equal to 2 as input and returns the count of all prime numbers from 1 to `n` (inclusive).
"""

def count_primes(n):
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False

    p = 2
    while p * p <= n:
        if is_prime[p] == True:
            for i in range(p * p, n+1, p):
                is_prime[i] = False
        p += 1

    count = sum(is_prime[2:])
    return count