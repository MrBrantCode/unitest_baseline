"""
QUESTION:
Write a function `calculate_standard_deviation(nums: List[int]) -> float` that takes a list of integers `nums` and returns the standard deviation as a float. The standard deviation is calculated by finding the mean, subtracting the mean from each number and squaring the result, calculating the mean of the squared differences, and taking the square root of the mean squared difference.
"""

from typing import List
import math

def calculate_standard_deviation(nums: List[int]) -> float:
    mean = sum(nums) / len(nums)
    squared_diff = [(x - mean) ** 2 for x in nums]
    mean_squared_diff = sum(squared_diff) / len(nums)
    standard_deviation = math.sqrt(mean_squared_diff)
    return standard_deviation