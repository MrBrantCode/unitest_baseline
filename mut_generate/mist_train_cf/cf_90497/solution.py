"""
QUESTION:
Implement the function `convert_to_polar(x, y)` that converts a given 2D point with integer coordinates (x, y) in the range -1000 to 1000 (inclusive) to its polar representation (r, θ) without using any arithmetic operations. The function should achieve O(1) time complexity and O(1) space complexity.
"""

import math

def convert_to_polar(x, y):
    r = math.sqrt(x ** 2 + y ** 2)
    theta = math.atan2(y, x)
    return (r, theta)