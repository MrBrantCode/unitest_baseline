"""
QUESTION:
Write a function named `prime_factor_product` that takes an integer `num` as input and returns the product of its prime factors. The function should handle large numbers efficiently.
"""

import math

def prime_factor_product(num):
    factors = []
    
    # divide by 2 until not divisible
    while num % 2 == 0:
        factors.append(2)
        num //= 2
        
    # iterate from 3 to sqrt(num) with step size of 2
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        while num % i == 0:
            factors.append(i)
            num //= i
            
    # if num is greater than 2, it is a prime number
    if num > 2:
        factors.append(num)
        
    # calculate the product of factors
    product = 1
    for factor in factors:
        product *= factor
        
    return product