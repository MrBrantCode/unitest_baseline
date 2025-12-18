"""
QUESTION:
Write a function `calculate_areas` that takes a list of tuples as input, where each tuple contains a base and height of a parallelogram. The function should return a list of areas, where each area is calculated as base * height, rounded to 2 decimal places. The function should be able to handle a large list of parallelograms and assume that the input tuples only contain positive decimal values.
"""

def calculate_areas(parallelograms):
    areas = []
    for base, height in parallelograms:
        area = round(base * height, 2)
        areas.append(area)
    return areas