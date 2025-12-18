"""
QUESTION:
Create a function called `is_prime(num)` that takes a number `num` as input and returns `True` if the number is prime, otherwise returns the smallest prime factor of the number. The function should be able to handle numbers up to 10^9 efficiently.
"""

import math

def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return i

    return True