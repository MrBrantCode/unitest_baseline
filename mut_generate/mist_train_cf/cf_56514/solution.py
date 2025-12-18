"""
QUESTION:
Design a function called classify_number(n) that takes an integer as input and returns 'square' if the number is a perfect square, 'prime' if the number is prime, and 'neither' otherwise. The function should handle integers greater than 1 and correctly identify perfect squares and prime numbers. Note that 1 is considered neither prime nor composite.
"""

import math

def classify_number(n):
    """
    This function returns 'square' for perfect square numbers, 'prime' for prime numbers, and 'neither' for the rest.
    """
    # Check if number is a perfect square
    sqrt = math.sqrt(n)
    if sqrt == int(sqrt):
        return 'square'

    # Check if number is a prime
    elif n > 1:
        for i in range(2, int(sqrt) + 1):
            if (n % i) == 0:
                return 'neither'
        return 'prime'

    else:
        return 'neither'