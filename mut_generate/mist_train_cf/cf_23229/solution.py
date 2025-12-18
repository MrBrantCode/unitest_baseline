"""
QUESTION:
Write a recursive function `is_prime(n, div=2)` that checks if a given number `n` is a prime number or not. The function should return `True` if `n` is prime and `False` otherwise. The function should also take an optional parameter `div` with default value 2.
"""

def entrance(n, div=2):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % div == 0:
        return False
    if div * div > n:
        return True
    return entrance(n, div + 1)