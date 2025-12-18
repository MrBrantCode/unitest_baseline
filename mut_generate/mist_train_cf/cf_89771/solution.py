"""
QUESTION:
Implement a function called "prime_factorization" that takes a positive integer as input and returns a list of its prime factors in ascending order without duplicates. The function should handle large numbers efficiently (e.g., up to 10^18) and return an error message if the input is not a positive integer.
"""

import math

def prime_factorization(n):
    if not isinstance(n, int) or n <= 0:
        return "Error: Input must be a positive integer."
    
    factors = []
    
    # Handle special cases for 1 and 0
    if n == 0 or n == 1:
        factors.append(n)
        return factors
    
    # Divide by 2 until it is no longer divisible
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    
    # Divide by odd numbers starting from 3
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    
    # If n is still greater than 2, it must be prime
    if n > 2:
        factors.append(n)
    
    return sorted(list(set(factors)))