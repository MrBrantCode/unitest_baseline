"""
QUESTION:
Write a function `is_right_equilateral_triangle` that determines if a triangle with sides of length a, b, and c is an equilateral right triangle and returns its area if it is, otherwise return None. The function should take three parameters a, b, and c and the triangle should meet the condition that the sum of any two sides is greater than the third side.
"""

def is_right_equilateral_triangle(a, b, c):
    sides = [a, b, c]
    sides.sort()
    if sides[0] == sides[1] == sides[2] and sides[0]**2 + sides[1]**2 == sides[2]**2:
        return 0.5 * sides[0] * sides[1]
    return None