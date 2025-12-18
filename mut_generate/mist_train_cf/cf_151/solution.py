"""
QUESTION:
Write a function named `is_prime` that takes a positive integer `n` greater than 1 as input and returns a boolean indicating whether `n` is a prime number, along with a list of its prime factors if it's not prime. The function should have a time complexity of O(sqrt(n)) or better.
"""

import math

def is_prime(n):
    factors = []
    for divisor in range(2, int(math.sqrt(n)) + 1):
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
    
    if n > 1:
        factors.append(n)
    
    if len(factors) == 1 and factors[0] == n:
        return True, None
    else:
        return False, factors