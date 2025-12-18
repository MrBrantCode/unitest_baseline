"""
QUESTION:
Implement a function `calculate_area_and_circumference(radius)` that calculates the area and circumference of a circle given the radius. The function should use the formulas area = π * radius^2 and circumference = 2 * π * radius, and return the results rounded to two decimal places. The function should also handle floating-point radii. 

Additionally, implement the following features in a `main` function: 
- Handle invalid input types, displaying an error message and asking the user to enter a valid numeric value.
- Validate the radius to be within a certain range (positive number not exceeding a maximum value).
- Allow the user to perform multiple calculations without terminating.
- Use a maximum allowed radius of 1000.
"""

import math

def calculate_area_and_circumference(radius):
    area = math.pi * radius**2
    circumference = 2 * math.pi * radius
    return round(area, 2), round(circumference, 2)