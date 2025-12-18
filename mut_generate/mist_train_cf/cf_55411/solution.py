"""
QUESTION:
Write a function `is_prime(n)` that takes an integer `n` and returns `True` if `n` is a prime number and `False` otherwise. Then, use a for loop to print all prime numbers from 1 to 100 in separate lines and calculate the summation of these prime numbers. The function `is_prime(n)` should not use built-in functions to check if a number is a prime.
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