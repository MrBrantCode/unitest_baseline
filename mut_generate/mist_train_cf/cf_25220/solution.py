"""
QUESTION:
Create a function `area(shape)` that calculates the area of a given shape. The shape can be a rectangle, triangle, or circle. The function should take user input for the necessary dimensions (length and width for rectangle, base and height for triangle, radius for circle) and return the calculated area.
"""

def calculate_area(shape, **kwargs):
    if shape == "rectangle":
        return kwargs['length'] * kwargs['width']
    elif shape == "triangle":
        return 0.5 * kwargs['base'] * kwargs['height']
    elif shape == "circle":
        return 3.14 * kwargs['radius'] * kwargs['radius']