"""
QUESTION:
Write a recursive function `triangle_area` that takes two parameters `b` and `h`, representing the base and height of a triangle, respectively. The function should calculate the area of the triangle using a recursive approach. Note that the area of a triangle is calculated as 0.5 times the base times the height, and the recursion stops when the height reaches 1.
"""

def triangle_area(b, h):
    if h == 1:
        return b
    else:
        return 0.5 * b + triangle_area(b, h-1)