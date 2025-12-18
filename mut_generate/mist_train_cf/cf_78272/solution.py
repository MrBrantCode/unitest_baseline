"""
QUESTION:
Write a function `is_prime(n)` that returns `True` if a number `n` is a prime number and `False` otherwise, and use it to print prime numbers between 0 and 100 that end with 3. The function should be optimized for performance by only checking divisibility up to the square root of `n`.
"""

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i:
            i += 2
        else:
            return False
    return True