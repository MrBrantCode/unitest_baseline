"""
QUESTION:
Create a function named `is_prime_and_perfect_square(n)` that takes a positive integer `n` as input and returns a boolean value indicating whether `n` is both a prime number and a perfect square. The function should have a time complexity of O(n^(1/4)) and a space complexity of O(1).
"""

import math

def is_prime_and_perfect_square(n):
    # Check if n is less than 2
    if n < 2:
        return False
    
    # Check if n is equal to 2 or 3
    if n == 2 or n == 3:
        return True
    
    # Check if n is divisible by 2 or 3
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Check if n is divisible by numbers of the form 6k ± 1
    sqrt_n = int(math.sqrt(n))
    for i in range(5, sqrt_n + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    
    # Check if n is a perfect square
    if int(math.sqrt(n))**2 == n:
        return True
    else:
        return False