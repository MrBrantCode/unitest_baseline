"""
QUESTION:
Write a function named `std_dev` that calculates the standard deviation of a given array of numbers, excluding any negative numbers from the calculation. The function should return the standard deviation.
"""

import math

def std_dev(nums):
    # Filter out non-negative numbers
    non_negative_nums = [num for num in nums if num >= 0]
    
    # Calculate the mean
    mean = sum(non_negative_nums) / len(non_negative_nums)
    
    # Calculate the variance
    variance = sum((num - mean) ** 2 for num in non_negative_nums) / len(non_negative_nums)
    
    # Calculate the standard deviation
    std_deviation = math.sqrt(variance)
    
    return std_deviation