"""
QUESTION:
Write a function named `is_prime(n)` that determines if a given number `n` is prime. The solution should have a time complexity of O(sqrt(n)) and must not use any built-in libraries, functions for prime number generation or factorization, loops, or recursion.
"""

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True