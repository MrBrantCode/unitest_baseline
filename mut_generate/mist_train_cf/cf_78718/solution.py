"""
QUESTION:
Create a function `is_prime(n)` that takes an integer `n` as input and returns `True` if the number is prime and `False` otherwise. Use this function to find and return all prime numbers between 50 and 70 (exclusive).
"""

def entrance(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True