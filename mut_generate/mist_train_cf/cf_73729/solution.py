"""
QUESTION:
Create a function `LCM` that takes a variable number of integer arguments and returns their lowest common multiple. The function should handle potential errors, including negative numbers and zero, and should be efficient in its calculation. If any of the input numbers is zero, the function should return zero.
"""

import math

def lcm_of_two(a, b):
    return abs(a*b) // math.gcd(a, b)

def LCM(*args):
    lcm = args[0]
    for num in args[1:]:
        if num != 0:
            lcm = lcm_of_two(lcm, num)
        else:
            return 0
    return lcm