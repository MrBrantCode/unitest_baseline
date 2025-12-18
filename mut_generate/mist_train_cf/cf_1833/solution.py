"""
QUESTION:
Create a function `is_prime()` to check if a number is prime. The function should take an integer as input, return `True` if the number is prime, and `False` otherwise. Then use this function to find and print all prime numbers in the list `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`, and calculate and print their sum.
"""

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True