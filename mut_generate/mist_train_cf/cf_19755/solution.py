"""
QUESTION:
Create a function called `is_prime(n)` that takes a positive integer `n` and returns a boolean indicating whether `n` is a prime number. The input `n` must be within the range of 2 to 10^9, inclusive. The solution should have a time complexity of O(sqrt(n)).
"""

import math

def entrance(n):
    # Check if number is within the valid range
    if n < 2 or n > 10**9:
        return False

    # Check divisibility from 2 to sqrt(n)
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True