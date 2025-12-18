"""
QUESTION:
Create a function that generates a dictionary of prime numbers from 1 to 100 as keys and their corresponding square roots as values. The function should not use any external libraries or modules. Define a helper function to check for prime numbers within the range.
"""

def is_prime(n):
    """Checks if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_dict():
    """Generates a dictionary of prime numbers from 1 to 100 as keys and their corresponding square roots as values."""
    return {i: i ** 0.5 for i in range(1, 101) if is_prime(i)}