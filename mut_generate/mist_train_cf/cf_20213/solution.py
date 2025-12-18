"""
QUESTION:
Implement a function `calculate_area` that takes in four parameters: the lengths of three sides of a triangle and the radius of its inscribed circle. The function should return the area of the triangle using the formula A = rs, where A is the area, r is the radius of the inscribed circle, and s is the semi-perimeter of the triangle. If the given sides cannot form a valid triangle, the function should return -1.
"""

def calculate_area(side1, side2, side3, radius):
    if side1 + side2 <= side3 or side2 + side3 <= side1 or side1 + side3 <= side2:
        return -1
    semi_perimeter = (side1 + side2 + side3) / 2
    area = semi_perimeter * radius
    return area