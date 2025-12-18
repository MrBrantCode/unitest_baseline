"""
QUESTION:
Write a function `area_triangle(a, b, c)` that calculates the area of a triangle using Heron's theorem and classifies the triangle as scalene, isosceles, or equilateral. The function should accept three parameters representing the lengths of the sides of the triangle, verify that these lengths form a legitimate triangle, and return the area and classification. If the lengths do not form a legitimate triangle, return -1. A triangle is considered legitimate if the sum of any two side lengths exceeds the length of the third side. The area should be returned to an accuracy of 2 decimal places.
"""

import math

def area_triangle(a, b, c):
    # Check if the input lengths can form a legitimate triangle
    if (a < b + c) and (b < a + c) and (c < a + b):
        
        # Compute semi-perimeter
        s = (a + b + c) / 2.0

        # Compute area using Heron's formula
        area = round(math.sqrt(s * (s - a) * (s - b) * (s - c)), 2)
        
        # Classify triangle
        if a == b == c:
            return area, 'Equilateral'
        elif a == b or b == c or c == a:
            return area, 'Isosceles'
        else:
            return area, 'Scalene'
    else:
        return -1