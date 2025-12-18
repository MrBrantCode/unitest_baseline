"""
QUESTION:
Create a function `is_prime(n)` that determines whether a given positive integer `n` is a prime number or not. The function should return `True` if `n` is prime and `False` otherwise. The input `n` is a positive integer and the function should not check for primality of numbers less than 2.
"""

def is_prime(n):
    # Check if number is less than 2
    if n < 2:
        return False
    
    # Check if number is divisible by any number from 2 to its square root
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    # If number is not divisible by any number from 2 to its square root, it is prime
    return True