"""
QUESTION:
Write a function `area_of_trapezoid(a, b, c, d)` that calculates the area of a trapezoid given the lengths of its four sides (a, b, c, d), where a and b are the lengths of the parallel sides, and c and d are the lengths of the non-parallel sides, with the constraints that the trapezoid has a perimeter of 20 units and is not a square.
"""

def area_of_trapezoid(a, b, c, d):
    h = abs(c - d) / 2
    return (h * (a + b)) / 2