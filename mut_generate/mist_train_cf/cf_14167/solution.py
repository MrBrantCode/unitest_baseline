"""
QUESTION:
Write a recursive function `calculate_surface_area(side_length)` that calculates the surface area of a cube given its side length. The function should not use any loops, only recursive calls. Assume the input side length is a positive integer.
"""

def calculate_surface_area(side_length):
    # Base case
    if side_length == 1:
        return 6
    
    # Recursive case
    return 6 * side_length * side_length - 6 * (side_length - 1) * (side_length - 1) + calculate_surface_area(side_length - 1)