"""
QUESTION:
Write a function `lcm_of_five_numbers(a, b, c, d, e)` that takes five positive integers as input and returns their least common multiple (LCM). The function should utilize the `lcm_two_numbers(a, b)` function, which calculates the LCM of two numbers using the formula `lcm(a, b) = (a * b) / gcd(a, b)`.
"""

import math

def lcm_of_five_numbers(a, b, c, d, e):
    # Calculate the LCM using the formula LCM(a, b) = (a * b) / GCD(a, b)
    def lcm_two_numbers(x, y):
        gcd = math.gcd(x, y)
        return (x * y) // gcd
    
    # Calculate the LCM of the first two numbers
    lcm = lcm_two_numbers(a, b)
  
    # Calculate the LCM of the result and the third number
    lcm = lcm_two_numbers(lcm, c)
  
    # Calculate the LCM of the result and the fourth number
    lcm = lcm_two_numbers(lcm, d)
  
    # Calculate the LCM of the result and the fifth number
    lcm = lcm_two_numbers(lcm, e)
  
    # Return the final LCM
    return lcm