"""
QUESTION:
Create a function `lcm_of_three` that calculates the Least Common Multiple (LCM) of three distinct positive integers not exceeding 10^5. The function should take three integers `a`, `b`, and `c` as input and return their LCM. The solution should be optimized for time complexity to run under 1 second.
"""

import math

def gcd(a, b):
    if a == 0: 
        return b 
    return gcd(b % a, a) 

def lcm(a, b): 
    return (a * b) // gcd(a, b) 

def lcm_of_three(a, b, c):
    return lcm(lcm(a, b), c)