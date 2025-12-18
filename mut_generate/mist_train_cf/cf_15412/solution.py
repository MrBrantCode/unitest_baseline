"""
QUESTION:
Create a function named `is_prime` that takes an integer `n` as input and returns `True` if the number is prime and `False` otherwise. The function should be optimized for time complexity. Use this function to print the prime numbers in reverse order from a given list.
"""

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True