"""
QUESTION:
Find the product of all prime numbers between two given numbers. 

Create a function named `is_prime` that takes an integer `n` as input and returns `True` if `n` is a prime number, and `False` otherwise. The input range will be between 1000 and 2000 (inclusive).
"""

def entrance(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True