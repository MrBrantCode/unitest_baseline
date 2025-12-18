"""
QUESTION:
Write a function `is_prime(num)` that takes an integer `num` as input and returns `True` if it's a prime number, `False` otherwise. Using this function, calculate the sum of all prime numbers between 1 and 100.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True