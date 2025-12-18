"""
QUESTION:
Write a function `largest_prime_factor(n)` that takes an integer `n` as input, where `n > 1` and `n` is not a prime number, and returns a tuple containing the largest prime factor of `n` and its occurrence.
"""

import math

def largest_prime_factor(n):
    """
    This function takes an integer n as input, where n > 1 and n is not a prime number,
    and returns a tuple containing the largest prime factor of n and its occurrence.
    
    Parameters:
    n (int): The input integer.
    
    Returns:
    tuple: A tuple containing the largest prime factor and its occurrence.
    """
    max_prime = -1
    count = 0
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            if i > max_prime:
                max_prime = i
                count = 1
            elif i == max_prime:
                count += 1
    if n > 1:
        if n > max_prime:
            max_prime = n
            count = 1
        elif n == max_prime:
            count += 1
    return max_prime, count