"""
QUESTION:
Implement a function `average_color_matching_functions()` that takes an instance of a color matching function class with a `get_values()` method, and returns the average value of the color matching functions. The function should calculate the average by summing up all the values and dividing by the total number of values.
"""

def average_color_matching_functions(color_matching_functions):
    values = color_matching_functions.get_values()
    average_value = sum(values) / len(values)
    return average_value