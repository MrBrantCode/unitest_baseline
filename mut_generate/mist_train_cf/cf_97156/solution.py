"""
QUESTION:
Write a function `is_prime(num)` that checks whether a given number is prime, where `num` is an integer. The function should return `True` if the number is prime and `False` otherwise.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True