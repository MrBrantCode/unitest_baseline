"""
QUESTION:
Write a function `calculate_surface_area` that calculates the surface area of a cube using only bitwise operations, given the side length of the cube as input. The function should return the calculated surface area.
"""

def calculate_surface_area(side_length):
    # Calculate the surface area using bitwise operations
    area = (side_length << 2) | (side_length << 1)
    return area