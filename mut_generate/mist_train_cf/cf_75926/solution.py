"""
QUESTION:
Create a function named `calculate_complicated_sum` that takes three parameters: `x`, `y`, and `z`. The function should calculate the sum of `x` and `y`, divide it by `z`, and then round up the result to the nearest integer. The function should return this final result.
"""

import math

def calculate_complicated_sum(x, y, z):
    # Finding the sum of x and y
    sum_value = x + y
    
    # Dividing the sum by z
    division_result = sum_value / z
    
    # Rounding this result to the nearest integer
    final_result = math.ceil(division_result)
    
    return final_result