"""
QUESTION:
Write a function `is_prime(n)` that determines whether a number `n` is prime. The function should return `True` if `n` is prime and `False` otherwise. Use this function to print all prime numbers between 2 and 100. The algorithm should be efficient and not brute-force all possible divisors.
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