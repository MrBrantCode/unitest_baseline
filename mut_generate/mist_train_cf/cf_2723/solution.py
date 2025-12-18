"""
QUESTION:
Create a function `sum_primes(N)` that calculates the sum of all prime numbers from `N` to `2N`, where `N` is a positive integer. The function should use a helper function `is_prime(n)` to check if a number is prime.
"""

def is_prime(n, i=2):
    if n <= 2:
        return n == 2
    if n % i == 0:
        return False
    if i * i > n:
        return True
    return is_prime(n, i + 1)

def sum_primes(N):
    def helper(n):
        if n <= N:
            return 0
        if is_prime(n):
            return n + helper(n - 1)
        return helper(n - 1)
    return helper(2 * N)