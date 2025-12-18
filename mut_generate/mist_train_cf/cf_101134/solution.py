"""
QUESTION:
Write a function `area_of_trapezoid(a, b, c, d)` that calculates the area of a trapezoid with sides of length a, b, c, and d, given the constraints that a and b are parallel, a + b + c + d = 20, c > d, c + d > a + b, c + a > b, and d + b > a.
"""

def area_of_trapezoid(a, b, c, d):
    h = abs(c - d) / 2
    return (h * (a + b)) / 2