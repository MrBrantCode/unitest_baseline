"""
QUESTION:
Write a function called `calculate_triangle_perimeter` that takes three parameters representing the lengths of the sides of a triangle, all of which must be integers greater than 0. The function should return the perimeter of the triangle.
"""

def calculate_triangle_perimeter(side1, side2, side3):
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        return "Side lengths must be greater than 0."
    
    perimeter = side1 + side2 + side3
    return perimeter