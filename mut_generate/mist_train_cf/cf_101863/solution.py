"""
QUESTION:
Write a function named `area_of_trapezoid` that takes four parameters a, b, c, d representing the lengths of the sides of a trapezoid. The function should calculate the area of the trapezoid, given that the perimeter is 20 units (a + b + c + d = 20) and a and b are the lengths of the parallel sides, with the restriction that a ≠ b and a + b < c + d.
"""

def area_of_trapezoid(a, b, c, d):
    h = abs(c - d) / 2
    return (h * (a + b)) / 2