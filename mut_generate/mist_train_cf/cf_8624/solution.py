"""
QUESTION:
Implement a function `convert_to_polar(x, y)` that takes two integer coordinates `x` and `y` between -1000 and 1000 (inclusive) as input and returns their corresponding polar representation `(r, θ)` without using arithmetic operations. The function should have a time complexity of O(1) and a space complexity of O(1).
"""

import math

def convert_to_polar(x, y):
    r = math.sqrt(x ** 2 + y ** 2)
    theta = math.atan2(y, x)
    return (r, theta)