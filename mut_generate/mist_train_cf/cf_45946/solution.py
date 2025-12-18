"""
QUESTION:
Write a function named `is_prime(n)` that checks if a given integer `n` is prime or not. The function should return `True` if `n` is a prime number and `False` otherwise. The function should be efficient and handle all integers, including edge cases. The input `n` will be a single integer, and there are no restrictions on its value. The output should be a boolean value indicating whether the input is prime or not.
"""

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True