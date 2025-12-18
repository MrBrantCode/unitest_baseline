"""
QUESTION:
Write a function `is_prime(num)` that takes an integer as input and returns `True` if the number is prime and `False` if it's composite. The function should work for numbers from 1 to 1000.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True