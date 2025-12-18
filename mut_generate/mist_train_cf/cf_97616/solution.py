"""
QUESTION:
Write a function `calculate_circumference` that calculates the circumference of a circle with a radius determined by the area of a larger shape, given that the circumference must not exceed a certain limit. The function should take two parameters: `A` (the area of the larger shape) and `k` (the maximum allowable circumference).
"""

import math

def calculate_circumference(A, k):
    r = math.sqrt(A/math.pi)  # Radius of the circle
    C = 2*math.pi*r  # Circumference of the circle
    
    if C > k:
        C = k
    return C