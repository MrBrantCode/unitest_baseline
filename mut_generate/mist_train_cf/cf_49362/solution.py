"""
QUESTION:
Create a function named `triangle_area` that calculates the area of a scalene triangle given the lengths of its three sides `a`, `b`, and `c`. The function should return the area with a precision of 4 decimal points. If the sides do not form a valid triangle, return `None`. If the calculated area is less than 0.0001, return a warning message. Use Heron's formula for efficient area calculation and validate the triangle's sides by ensuring the sum of any two sides is greater than the third side.
"""

def triangle_area(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        p = (a + b + c) / 2
        area = (p*(p-a)*(p-b)*(p-c))**0.5
        area = round(area, 4) 
        if area < 0.0001:
            return "Warning: the area is very small (< 0.0001)."
        else:
            return area
    else:
        return None