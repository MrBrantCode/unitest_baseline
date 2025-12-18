"""
QUESTION:
Write a function named `calculate_area` that takes in two positive integers, `length` and `width`, and returns the area of a rectangle. The area should be calculated by multiplying the length by the width. If the calculated area exceeds 200, return the string "Area too large". Otherwise, return the calculated area.
"""

def calculate_area(length, width):
    area = length * width
    if area > 200:
        return "Area too large"
    else:
        return area