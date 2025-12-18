"""
QUESTION:
Create a function named `is_product_prime` that takes a list of non-negative integers as input and returns a Boolean indicating whether the product of the numbers in the list results in a prime number. The function should efficiently handle lists containing large numbers (up to 10^9) or a large number of elements (up to 10^6).
"""

import math

def is_product_prime(lst):
    # if the list has more than one number, the function returns false
    if len(lst) > 1: 
        return False 
    else:
        # if the list has only one number, check if it's prime
        n = lst[0]
        if n == 1: 
            return False 
        elif n == 2: 
            return True 
        else: 
            # check divisors up to square root of n
            for i in range(2, math.isqrt(n) + 1): 
                if n % i == 0: 
                    return False 
            return True