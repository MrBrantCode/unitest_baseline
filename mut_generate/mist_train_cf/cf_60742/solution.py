"""
QUESTION:
Implement a function `get_primes` that takes a list of integers as input and returns a list of all prime numbers from the input list. The function should be optimized for large input lists containing up to 10^5 integers.
"""

import math

def get_primes(input_list):
    result_list = []
    for element in input_list:
        if element > 1:  
            is_prime = True
            for i in range(2, math.isqrt(element) + 1): 
                if element % i == 0:  
                    is_prime = False
                    break
            if is_prime:
                result_list.append(element)
    return result_list