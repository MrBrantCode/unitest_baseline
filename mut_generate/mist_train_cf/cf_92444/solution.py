"""
QUESTION:
Create a function `calculate_area` that calculates the area of a triangle using Heron's formula, given the lengths of all three sides. The function should take three parameters, each representing the length of a side of the triangle, and return the area of the triangle. The function should handle the calculation using Heron's formula internally.
"""

def calculate_area(side1, side2, side3):
    semi_perimeter = (side1 + side2 + side3) / 2
    area = (semi_perimeter * (semi_perimeter - side1) * (semi_perimeter - side2) * (semi_perimeter - side3)) ** 0.5
    return area