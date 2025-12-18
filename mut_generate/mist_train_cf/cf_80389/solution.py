"""
QUESTION:
Design a function named `lcm_of_three` that calculates the Least Common Multiple (LCM) of three distinct positive integers. The function should be able to handle numbers with large magnitudes and be optimized for speed. The LCM of the three numbers should be calculated using the associative property of LCM, i.e., lcm(a,lcm(b,c)) = lcm(lcm(a,b),c).
"""

import math

def lcm_of_three(a, b, c):
    def gcd(x, y):
        return math.gcd(x, y)
    
    def lcm(x, y):
        return x * y // gcd(x, y)

    return lcm(lcm(a, b), c)