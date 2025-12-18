"""
QUESTION:
Write a function `is_valid_triangle(a, b, c)` that determines whether three given side lengths `a`, `b`, and `c` can form a valid triangle, with the restriction that the sum of the lengths of any two sides must be greater than the length of the third side. The function should return `True` if the side lengths form a valid triangle and `False` otherwise. Assume that the input values are non-negative and the triangle can be isosceles.
"""

def entance(a, b, c):
    if (a + b) > c and (a + c) > b and (b + c) > a:
        return True
    else:
        return False