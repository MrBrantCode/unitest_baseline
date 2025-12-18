"""
QUESTION:
Implement a function `calculate_circumference` that calculates the circumference of a circle given the area of the larger shape it is part of and a maximum allowable circumference. The function should take two parameters, `A` (the area of the larger shape) and `k` (the maximum allowable circumference), and return the circumference of the circle, not exceeding the maximum allowable value.
"""

import math

def calculate_circumference(A, k):
    r = math.sqrt(A/math.pi)
    C = 2*math.pi*r
    if C > k:
        C = k
    return C