"""
QUESTION:
Create a function `calculate_area` that takes three string arguments representing the side lengths of a triangle. The function should convert these strings to integers, check if they can form a valid triangle, and if so, calculate the area using Heron's formula. The calculated area should be rounded to two decimal places. If the sides cannot form a valid triangle or if the input strings cannot be converted to integers, the function should return an error message.
"""

import math

def calculate_area(side1, side2, side3):
    try:
        a = int(side1)
        b = int(side2)
        c = int(side3)
        
        if a + b > c and a + c > b and b + c > a:
            s = (a + b + c) / 2
            area = math.sqrt(s * (s - a) * (s - b) * (s - c))
            return round(area, 2)
        else:
            return "The given sides cannot form a valid triangle."
    except ValueError:
        return "Invalid input. Sides must be integers."