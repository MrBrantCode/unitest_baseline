"""
QUESTION:
Create a function `is_prime(n)` that takes an integer `n` as input and returns `True` if the number is prime and `False` otherwise. The function should optimize the prime check by only checking divisibility up to the square root of `n`. Use this function to filter a list of numbers and return a list of prime numbers.
"""

import math

def is_prime(n):
    if n <= 1 or (n % 2 == 0 and n > 2): 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))