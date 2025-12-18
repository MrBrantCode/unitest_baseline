"""
QUESTION:
Write a function called `calculate_area` that takes the lengths of the three sides of a triangle as arguments (a, b, c) and returns the area of the triangle. The sides must satisfy the triangle inequality (the sum of the lengths of any two sides must be greater than the length of the third side), but you do not need to check for this condition. Use Heron's formula to calculate the area.
"""

def calculate_area(a, b, c):
    # calculate the semi-perimeter
    s = (a + b + c) / 2
    # calculate the area
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    return area