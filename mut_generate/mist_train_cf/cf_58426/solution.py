"""
QUESTION:
Create a function named `prime_length` that takes a string as input, calculates its length, and returns `True` if the length is a prime number and `False` otherwise. The function should utilize a helper function named `is_prime` that checks whether a given number is prime. The `is_prime` function should be able to handle numbers less than 2 and should only check divisibility up to the square root of the number.
"""

def is_prime(n):
    """Validate if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_length(string):
    """Accept a string, get its length, and verify if 
    the length is a prime number."""
    length = len(string)
    return is_prime(length)