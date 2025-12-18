"""
QUESTION:
Write a function `rectangular_cuboid_surface_area` that calculates the surface area of a rectangular cuboid given its length, width, and height. The function should take three parameters: length (l), width (w), and height (h) and return the total surface area. The surface area of a cuboid is given by the formula: 2lw + 2lh + 2wh.
"""

def rectangular_cuboid_surface_area(length, width, height):
    return 2*length*width + 2*length*height + 2*width*height