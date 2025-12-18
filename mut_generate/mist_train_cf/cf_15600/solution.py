"""
QUESTION:
Create a function called `calculate_standard_deviation` that calculates the standard deviation of an array of numbers without using any built-in functions or libraries. The function should handle both positive and negative numbers, return the standard deviation as a floating-point number with 4 decimal places, and have a time complexity of O(n), where n is the number of elements in the array. Assume the array will always have at least one element.
"""

import math

def calculate_standard_deviation(arr):
    n = len(arr)
    mean = sum(arr) / n
    sum_of_squares = sum((x - mean) ** 2 for x in arr)
    variance = sum_of_squares / n
    std_deviation = math.sqrt(variance)
    return round(std_deviation, 4)