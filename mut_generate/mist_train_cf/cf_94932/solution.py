"""
QUESTION:
Create a function called `is_prime_gt_100` that takes one argument. The function should return `True` if the argument is a prime number greater than 100, and `False` otherwise. The function should use an efficient algorithm to check for primality, considering that any composite number must have a factor less than or equal to its square root.
"""

import math

def is_prime_gt_100(value):
    if value <= 100:
        return False

    for i in range(2, int(math.sqrt(value)) + 1):
        if value % i == 0:
            return False

    return True