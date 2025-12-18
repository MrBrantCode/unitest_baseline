"""
QUESTION:
Write a function named `find_triangle_area` that takes two parameters, `base` and `height`, and returns the area of a triangle using the formula `A = 0.5 * base * height`. Ensure that `base` and `height` are both positive integers, and the calculated area is rounded to the nearest integer. If `base` or `height` is not a positive integer, return "Invalid input".
"""

def find_triangle_area(base, height):
    if type(base) != int or type(height) != int or base <= 0 or height <= 0:
        return "Invalid input"

    area = 0.5 * base * height
    area = round(area)

    return area