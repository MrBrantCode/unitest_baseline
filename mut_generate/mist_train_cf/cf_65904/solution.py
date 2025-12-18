"""
QUESTION:
Create a function `update_array_elements` that takes a list of integers as input and updates each element in the list. If the list contains at least one prime number, update each element by dividing it by the square root of the smallest prime number in the list. If no prime numbers are found in the list, update each element by dividing it by the maximum number in the list.
"""

import numpy as np
import math

def is_prime(n):
    """Check if number is prime."""
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_div = math.floor(math.sqrt(n))
    for i in range(3, 1 + max_div, 2):
        if n % i == 0:
            return False
    return True

def update_array_elements(a):
    """Update each element in the list."""
    prime_in_a = [x for x in a if is_prime(x)]
    if len(prime_in_a) > 0:
        return a / np.sqrt(min(prime_in_a))
    else:
        return a / max(a)