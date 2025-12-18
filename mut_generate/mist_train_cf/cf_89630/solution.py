"""
QUESTION:
Write a function named `calculate_sum_of_areas` that takes a list of dictionaries representing circles. Each dictionary must contain 'radius', 'x', and 'color' as keys, where 'radius' is an integer between 1 and 10, 'x' is a float between 0 and 100, and 'color' is a string consisting of only lowercase alphabetic characters with a length between 1 and 10. The list must contain between 1 and 1000 circles. The function should return the sum of the areas of the circles rounded to two decimal places and print the color of the circle with the largest area.
"""

import math

def calculate_sum_of_areas(circles):
    max_area = 0
    max_color = ""
    sum_of_areas = 0
    
    for circle in circles:
        radius = circle.get('radius', 0)
        x = circle.get('x', 0)
        color = circle.get('color', "")
        
        if 1 <= radius <= 10 and 0 <= x <= 100 and 1 <= len(color) <= 10:
            area = math.pi * radius**2
            sum_of_areas += area
            
            if area > max_area:
                max_area = area
                max_color = color
        
    print(f"The color of the circle with the largest area is {max_color}")
    return round(sum_of_areas, 2)