"""
QUESTION:
Write a function `is_prime` that takes an integer `n` as input and returns `True` if `n` is a prime number and `False` otherwise. Use this function to find all prime numbers in the range between 1 to 1000 (inclusive) and calculate their sum. The function should not take any other parameters.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True