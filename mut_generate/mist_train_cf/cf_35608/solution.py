"""
QUESTION:
Write a function `calculate_variable_sum(variables: List[str]) -> int` that takes in a list of variable names and returns the sum of the values of these variables. The function should consider only the variables provided in the input list, ignore any other variables, and use the predefined variable values: c23_2d = 0, c24_2d = 0, up2_2d = 0, c30_2d = 0, c31_2d = 0, c32_2d = 0, c33_2d = 0, c34_2d = 0.
"""

from typing import List

def calculate_variable_sum(variables: List[str]) -> int:
    variable_values = {
        'c23_2d': 0,
        'c24_2d': 0,
        'up2_2d': 0,
        'c30_2d': 0,
        'c31_2d': 0,
        'c32_2d': 0,
        'c33_2d': 0,
        'c34_2d': 0,
    }
    return sum(variable_values[var] for var in variables if var in variable_values)