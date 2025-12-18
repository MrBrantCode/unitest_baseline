"""
QUESTION:
Create a function called `is_prime(n)` that determines whether a given number `n` is a prime number. The function should have a time complexity of O(sqrt(n)). The input `n` is an integer, and the function should return a boolean value indicating whether the number is prime.
"""

import math

def entrance(n):
    if n <= 1:
        return False
    
    if n == 2:
        return True
    
    if n % 2 == 0:
        return False
    
    sqrt_n = int(math.sqrt(n)) + 1
    for i in range(3, sqrt_n, 2):
        if n % i == 0:
            return False
    
    return True