"""
QUESTION:
Write a function `calculate_circle_areas` that takes a list of radii as input and returns a list of the corresponding circle areas, calculated using the formula A = πr². The function should use the math library for the value of π and return areas with two decimal places.
"""

import math

def calculate_circle_areas(radii):
    """
    Calculate the areas of circles given a list of radii.

    Args:
        radii (list): A list of radii.

    Returns:
        list: A list of corresponding circle areas.
    """
    areas = []
    for r in radii:
        area = math.pi * r**2
        areas.append(round(area, 2))
    return areas