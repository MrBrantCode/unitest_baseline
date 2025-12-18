"""
QUESTION:
Create a function named `generate_pink_shades` that generates 'n' different shades of pink, each darker than the previous one. The function should take one argument 'n' representing the number of shades to be generated and return a list of 'n' RGB color tuples, where each tuple represents a shade of pink. The shades should be visibly different from each other, with the first shade being the lightest and the last shade being the darkest.
"""

import colorsys

def generate_pink_shades(n):
    """
    Generates 'n' different shades of pink, each darker than the previous one.
    
    Args:
    n (int): The number of shades to be generated.
    
    Returns:
    list: A list of 'n' RGB color tuples, where each tuple represents a shade of pink.
    """
    base_color = (1.0, 0.75, 0.80) # This is a light pink color
    min_darkness = 0.1
    max_darkness = 0.9
    darkness_increment = (max_darkness - min_darkness) / n
    return [colorsys.hsv_to_rgb(base_color[0], base_color[1], base_color[2] * (min_darkness + i * darkness_increment)) for i in range(n)]