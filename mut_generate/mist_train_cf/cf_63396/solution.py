"""
QUESTION:
Create a function called `complex_triangle_solver` that takes three parameters, `a`, `b`, and `c`, representing the lengths of the sides of a triangle. 

Using Heron's formula, calculate the area of the triangle to 2 decimal places and identify the type of triangle as 'Scalene', 'Isosceles', or 'Equilateral'. Return the calculated area and the type of triangle. 

If the sides do not form a valid triangle (the sum of any two sides must be greater than the third side), return -1.
"""

import math

def complex_triangle_solver(a, b, c):
    # Check if triangle is valid
    if a + b <= c or a + c <= b or b + c <= a:
        return -1

    # Calculate the semi-perimeter
    s = (a + b + c) / 2

    # Calculate the area using Heron's formula
    area = float("%.2f" % (math.sqrt(s*(s-a)*(s-b)*(s-c))))

    # Check for type of triangle
    if a == b == c :
        return (area, 'Equilateral')
    elif a == b or a == c or b == c:
        return (area, 'Isosceles')
    else:
        return (area, 'Scalene')