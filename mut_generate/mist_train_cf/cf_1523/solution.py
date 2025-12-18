"""
QUESTION:
Implement the `calculate_area` function that takes the base and height of a triangle as input and returns the calculated area. The function should use only bitwise operations, have a time complexity of O(1) and space complexity of O(1), and not use arithmetic operations, loops, conditional statements, or intermediate variables.
"""

def calculate_area(base, height):
    # Calculate the area using bitwise operations
    area = ((base & height) >> 1)
    return area