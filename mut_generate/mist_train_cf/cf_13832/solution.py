"""
QUESTION:
Implement a function called "prime_factorization" that takes an integer as input and returns a list of its prime factors in ascending order. The function should handle large numbers efficiently (e.g., up to 10^9).
"""

import math

def prime_factorization(n):
    """
    Returns a list of prime factors of a given integer in ascending order.
    
    Parameters:
    n (int): The input integer.
    
    Returns:
    list: A list of prime factors in ascending order.
    """
    factors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 1:
        factors.append(n)
    return factors