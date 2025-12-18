"""
QUESTION:
Create a function named `is_prime` that checks whether a number is prime or not and use it to print all prime numbers in the range from 10^6 to 1 in reverse order.
"""

import math

def entrance(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True