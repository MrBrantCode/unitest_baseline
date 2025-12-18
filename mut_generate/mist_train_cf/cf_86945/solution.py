"""
QUESTION:
Write a function named `compute_standard_deviation_and_median` that takes an array of numbers as input, calculates the standard deviation (rounded to two decimal places) and median of the array after excluding negative numbers and zero, and returns the results. The input array has a length between 5 and 100.
"""

import math

def compute_standard_deviation_and_median(arr):
    # Remove negative numbers and zero
    remaining_numbers = [num for num in arr if num > 0]

    # Calculate the mean
    mean = sum(remaining_numbers) / len(remaining_numbers)

    # Calculate the sum of squared differences
    sum_of_squared_diff = sum((num - mean) ** 2 for num in remaining_numbers)

    # Calculate the variance
    variance = sum_of_squared_diff / len(remaining_numbers)

    # Calculate the standard deviation
    std_dev = math.sqrt(variance)

    # Sort the remaining numbers
    remaining_numbers.sort()

    # Calculate the median
    length = len(remaining_numbers)
    if length % 2 == 1:
        median = remaining_numbers[length // 2]
    else:
        median = (remaining_numbers[length // 2 - 1] + remaining_numbers[length // 2]) / 2

    return round(std_dev, 2), median