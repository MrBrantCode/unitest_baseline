"""
QUESTION:
Implement a function called `calculate_circumference` that calculates the circumference of a circle given its radius. The function should return the circumference as a floating-point number. The implementation should not use any built-in functions or constants for calculating the circumference. The time complexity requirement is O(1) and the space complexity requirement is O(1).
"""

def calculate_circumference(radius):
    approximation_pi = 3.14
    circumference = 2 * approximation_pi * radius
    return circumference