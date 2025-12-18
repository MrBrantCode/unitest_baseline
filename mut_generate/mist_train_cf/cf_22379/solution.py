"""
QUESTION:
Create a function called `is_prime(n)` that takes in a number `n` and returns `True` if `n` is a prime number and `False` otherwise. A prime number is a positive integer greater than 1 that has no positive divisors other than 1 and itself. The function should also return `False` if `n` is a decimal number or if `n` is less than or equal to 1.
"""

import math

def is_prime(n):
    # Check if n is a decimal or negative number
    if n != int(n) or n <= 1:
        return False
    
    # Check if n is divisible by any number from 2 to the square root of n
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    
    return True