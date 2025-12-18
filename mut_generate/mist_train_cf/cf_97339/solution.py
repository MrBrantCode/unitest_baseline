"""
QUESTION:
Write a function `calculate_area(side_length)` that calculates the area of an equilateral triangle given the side length. The function should only accept a positive integer or floating-point number as input and return the calculated area rounded to two decimal places. If the input is invalid, the function should return an error message.
"""

def entance(side_length):
    if isinstance(side_length, (int, float)) and side_length > 0:
        area = (3**0.5 * side_length**2) / 4
        return round(area, 2)
    else:
        return "Invalid input value for side length"