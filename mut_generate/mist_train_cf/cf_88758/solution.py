"""
QUESTION:
Create a function `is_prime(n)` that takes a positive integer `n` as input and returns `True` if `n` is a prime number, `False` otherwise, and an error message if `n` is outside the range of 2 to 10^18, inclusive. The function should have a time complexity of O(sqrt(n)).
"""

import math

def is_prime(n):
    if n < 2 or n > 10**18:
        return "Input must be between 2 and 10^18, inclusive."
    elif n > 10**9:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True