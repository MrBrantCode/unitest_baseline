"""
QUESTION:
Given a function named `calculate_circle_area` that takes a positive integer `radius` between 1 and 10^18 (inclusive) as input, calculate the area of a circle using the formula Area = pi * r * r. The solution should have a time complexity of O(1) and a space complexity of O(1). Only basic arithmetic operations (+, -, *, /) and the math constant pi can be used.
"""

import math

def calculate_circle_area(radius):
    return math.pi * radius * radius