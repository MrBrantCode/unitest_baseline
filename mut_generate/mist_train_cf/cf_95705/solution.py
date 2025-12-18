"""
QUESTION:
Create a function named `is_prime` that takes an integer `num` as input. The function should return `True` if `num` is a prime number and `False` otherwise. Use this function to find the sum of all prime numbers up to and including 1000.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True