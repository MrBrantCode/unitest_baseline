"""
QUESTION:
Write a function `categorizeNumbers(arr)` that categorizes elements of an input array into prime numbers, composite numbers (including 0 and 1), and non-integer numbers. The function should handle negative numbers and decimal numbers correctly and return three separate lists: primes, composites, and non_integers.
"""

import math

def is_prime(n):
    if n < 2: 
        return False
    if n == 2 or n == 3: 
        return True
    if n % 2 == 0 or n % 3 == 0: 
        return False
    for i in range(5, int(n**0.5) + 1, 6): 
        if n % i == 0 or n % (i + 2) == 0: 
            return False
    return True

def categorizeNumbers(arr):
    primes = []
    composites = []
    non_integers = []
    for num in arr:
        if isinstance(num, int):
            if num > 1 and is_prime(num): 
                primes.append(num)
            elif num >= 0: 
                composites.append(num)
        else:
            non_integers.append(num)
    return primes, composites, non_integers