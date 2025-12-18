"""
QUESTION:
Write a function `compute_standard_deviation_and_median` that takes an array of integers as input. The function should calculate the standard deviation of the array, excluding any negative numbers and zero, rounded to two decimal places. The function should also calculate and return the median of the array after excluding the negative numbers and zero. The input array will have a minimum length of 5 and a maximum length of 100.
"""

import math

def compute_standard_deviation_and_median(arr):
    # Remove negative numbers and zero
    remaining_numbers = [num for num in arr if num > 0]

    # Calculate the mean
    mean = sum(remaining_numbers) / len(remaining_numbers)

    # Calculate the sum of squared differences
    sum_of_squared_diff = sum((num - mean) ** 2 for num in remaining_numbers)

    # Divide the sum of squared differences by the number of remaining numbers
    variance = sum_of_squared_diff / len(remaining_numbers)

    # Take the square root to find the standard deviation
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