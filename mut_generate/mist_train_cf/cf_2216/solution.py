"""
QUESTION:
Write a function `calculate_circle_area` that takes a positive integer `radius` between 1 and 10^18 (inclusive) as input and returns the area of a circle using the formula Area = pi * r * r, where pi is approximated as 3.14159. The solution must use only basic arithmetic operations (+, -, *, /) and handle extremely large radius values within a reasonable time frame, with a time complexity of O(1) and a space complexity of O(1).
"""

def calculate_circle_area(radius):
    integer_part = int(radius)
    decimal_part = radius - integer_part

    area_integer_part = 3.14159 * integer_part * integer_part
    area_decimal_part = 3.14159 * decimal_part * decimal_part

    return area_integer_part + area_decimal_part