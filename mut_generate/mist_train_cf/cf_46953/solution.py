"""
QUESTION:
Create a function named `lcm_three_numbers` that takes four parameters: three integers `a`, `b`, `c`, and a modulus `n`. The function should calculate and return the least common multiple (LCM) of `a`, `b`, and `c` modulo `n`. The function should efficiently handle large numbers and should be able to return the correct result even when `a`, `b`, and `c` are large. Assume that `a`, `b`, `c`, and `n` are positive integers greater than zero.
"""

import math

def lcm_three_numbers(a, b, c, n):
    def lcm_two_numbers(a, b):
        return a * b // math.gcd(a, b)
    
    return lcm_two_numbers(lcm_two_numbers(a, b), c) % n