"""
QUESTION:
Create a function `triangle_area(a, b, c)` that calculates and returns the area of a triangle with sides of lengths `a`, `b`, and `c`. The area should be returned with a precision of 2 decimal points. If the sides cannot form a valid triangle (i.e., the sum of any two sides is not greater than the length of the third side), return -1.
"""

def triangle_area(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return round(area, 2)
    else:
        return -1