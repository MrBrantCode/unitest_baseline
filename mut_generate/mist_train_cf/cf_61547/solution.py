"""
QUESTION:
Write a function `is_prime(n)` that checks if a given number `n` is prime, considering negative numbers as non-prime. Then, create a 4-D matrix named "B" of size (10,10,10,10) populated with random integers from -1000 to 1000 inclusive, flatten it to a 1-D array, and efficiently find all prime numbers in the 1-D array using the `is_prime(n)` function.
"""

import numpy as np

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True