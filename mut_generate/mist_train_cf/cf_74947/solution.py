"""
QUESTION:
Given a rectangle with a length that is twice its breadth and a perimeter of 30 cm, write a function named `rectangle_dimensions_and_area` that calculates the length, breadth, and area of the rectangle. The function should take the perimeter as an input parameter and return the length, breadth, and area as output.
"""

def rectangle_dimensions_and_area(perimeter):
    breadth = perimeter / 6
    length = 2 * breadth
    area = length * breadth
    return length, breadth, area