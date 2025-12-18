"""
QUESTION:
Create a function named `compute_lcm` that takes three distinct non-negative and non-zero integers `a`, `b`, and `c` as input and returns their Least Common Multiple (LCM). The function should have a time complexity of O(log(min(A, B)) + log(min(LCM(A, B), C))) and should be efficient and readable.
"""

import math

def compute_lcm(a, b, c):
    temp = a * b // math.gcd(a, b)
    lcm = temp * c // math.gcd(temp, c)
    return lcm