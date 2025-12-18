"""
QUESTION:
Write a function `is_prime(num)` that takes an integer as input and returns `True` if it is a prime number and `False` otherwise. Then use this function to print all prime numbers in the range 1 to 100.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True