"""
QUESTION:
Create a function named `calculate_lcm` that takes two positive integers `x` and `y` as input and returns their least common multiple (LCM). The function should handle edge cases, including the scenario where either `x` or `y` is zero. The LCM should be calculated using the mathematical rule that LCM of two numbers is the absolute value of the product of the numbers divided by their Greatest Common Divisor (GCD).
"""

import math

def calculate_lcm(x: int, y: int) -> int:
    """ Return the LCM of two integers x and y """
    if x == 0 or y == 0:  
        return 0
    else:        
        return abs(x * y) // math.gcd(x, y)