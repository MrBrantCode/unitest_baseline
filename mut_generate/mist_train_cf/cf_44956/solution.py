"""
QUESTION:
Define a function `stealthy_numbers(limit)` that returns the quantity of stealthy numbers that do not exceed the given limit. A stealthy number is a positive integer N that can be expressed as the product of two distinct pairs of positive integers (a, b) and (c, d) such that a*b = c*d = N and a+b = c+d+1. The function should only consider integers N that do not surpass the given limit.
"""

import math

def stealthy_numbers(limit):
    """
    Returns the quantity of stealthy numbers that do not exceed the given limit.
    
    A stealthy number is a positive integer N that can be expressed as the product 
    of two distinct pairs of positive integers (a, b) and (c, d) such that 
    a*b = c*d = N and a+b = c+d+1.
    """
    count = 0
    max_a = int(limit**0.5)
    
    for a in range(1, max_a+1):
        max_c = min(a, ((limit-a*a)//(2*a))**0.5)
        count += int(max_c)
    count += max_a * (max_a-1) // 2  # account for a = c case
    
    return count