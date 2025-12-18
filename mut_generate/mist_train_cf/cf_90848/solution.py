"""
QUESTION:
Create a function named `find_triangle_area` that calculates the area of a triangle given its base and height. The base and height must be positive integers. The function should return the calculated area rounded to the nearest integer. If either the base or height is not a positive integer, the function should return "Invalid input".
"""

def find_triangle_area(base, height):
    # Check if base and height are positive integers
    if type(base) != int or type(height) != int or base <= 0 or height <= 0:
        return "Invalid input"

    # Calculate the area using the formula
    area = 0.5 * base * height

    # Round the area to the nearest integer
    area = round(area)

    return area