"""
QUESTION:
Write a Python function named `area_of_trapezoid` that calculates the area of a trapezoid given the lengths of its four sides a, b, c, and d. The trapezoid has a perimeter of 20 units, and a and b are the lengths of the parallel sides. The function should return the area of the trapezoid.
"""

def area_of_trapezoid(a, b, c, d):
    h = abs(c - d) / 2
    return (h * (a + b)) / 2