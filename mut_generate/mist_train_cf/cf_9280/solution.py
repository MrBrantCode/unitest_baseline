"""
QUESTION:
Create a function named `is_prime` that takes a positive integer greater than 1 and returns `True` if it is a prime number, and `False` otherwise.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True