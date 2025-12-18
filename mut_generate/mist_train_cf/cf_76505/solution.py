"""
QUESTION:
Write a function named `calculate_processing_speed` that calculates the predicted processing speed after a specified number of years, given an initial processing speed. The function should assume that processing speed doubles every two years. The function should take two parameters: `initial_speed` and `years`. The function should return the predicted processing speed after the specified number of years.
"""

def calculate_processing_speed(initial_speed, years):
    return initial_speed * (2 ** (years // 2))