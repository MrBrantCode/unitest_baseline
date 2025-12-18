"""
QUESTION:
Write a function `calculate_standard_deviation(nums: List[int]) -> float` that takes in a list of integers `nums` and returns the standard deviation as a float. The function should calculate the standard deviation manually without using any built-in libraries or functions for calculating standard deviation or mean.
"""

from typing import List

def entrance(nums: List[int]) -> float:
    mean = sum(nums) / len(nums)
    
    squared_diff = [(num - mean)**2 for num in nums]
    mean_squared_diff = sum(squared_diff) / len(nums)
    
    standard_deviation = mean_squared_diff ** 0.5
    return standard_deviation