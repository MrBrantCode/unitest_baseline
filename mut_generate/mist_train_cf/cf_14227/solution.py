"""
QUESTION:
Create a function `calculate_triangle_area(a, b, c)` that calculates the area of a triangle given the lengths of all three sides `a`, `b`, and `c`. The function should return the area rounded to the nearest whole number. If the triangle is not valid (i.e., the sum of any two sides is less than or equal to the third side), the function should return "Invalid triangle". Assume that the input lengths of the sides are positive real numbers.
"""

import math

def calculate_triangle_area(a, b, c):
    if (a + b <= c) or (b + c <= a) or (c + a <= b):
        return "Invalid triangle"
    
    s = (a + b + c) / 2
    
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    return round(area)