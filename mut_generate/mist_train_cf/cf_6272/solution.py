"""
QUESTION:
Create a function `calculate_circle` that takes a required parameter `radius` and an optional parameter `decimal_place` (defaulting to 2) to calculate the area and circumference of a circle. The function should use the formulas A = πr^2 for area and C = 2πr for circumference, utilizing the math library's value of pi for precision. The function should then round the calculated area and circumference to the specified decimal place before returning the values.
"""

import math

def calculate_circle(radius, decimal_place=2):
    area = math.pi * radius**2
    circumference = 2 * math.pi * radius
    
    # rounding the values to specified decimal place
    area = round(area, decimal_place)
    circumference = round(circumference, decimal_place)
    
    return area, circumference