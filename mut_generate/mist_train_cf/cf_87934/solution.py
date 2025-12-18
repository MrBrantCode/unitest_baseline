"""
QUESTION:
Write a function named `calculate_sum` that takes an array of float values and returns the sum of its non-negative elements (excluding values greater than 100) rounded to two decimal places. The function should be able to handle large arrays (up to 10^6 elements) efficiently.
"""

def calculate_sum(array):
    return round(sum(value for value in array if 0 <= value <= 100), 2)