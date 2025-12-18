"""
QUESTION:
Write a function `sum_of_areas` to calculate the sum of the areas of a list of circles. Each circle is a dictionary with 'radius' (positive integer) and 'x' (positive float) keys. The list must contain 1-100 circles. The function should return the sum of the areas rounded to two decimal places.
"""

import math

def sum_of_areas(circles):
    if not circles or len(circles) < 1 or len(circles) > 100:
        return "Invalid input"

    sum_areas = 0
    for circle in circles:
        if 'radius' not in circle or 'x' not in circle:
            return "Invalid input"
        if not isinstance(circle['radius'], int) or circle['radius'] <= 0:
            return "Invalid input"
        if not isinstance(circle['x'], float) or circle['x'] <= 0:
            return "Invalid input"
        
        area = math.pi * (circle['radius'] ** 2)
        sum_areas += area

    return round(sum_areas, 2)