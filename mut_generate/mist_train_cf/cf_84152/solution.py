"""
QUESTION:
Find the smallest positive integer that represents the number of Earth days three celestial bodies with orbital periods of 360, 450, and 540 days will take to align in the same positions again.

Create a function named `lcm` that takes two arguments and returns their Least Common Multiple. Use this function to find the LCM of the three orbital periods and output the result.
"""

import math

def find_alignment_days(a, b, c):
    def lcm(x, y):
        return x * y // math.gcd(x, y)

    temp = lcm(a, b)
    result = lcm(temp, c)
    return result