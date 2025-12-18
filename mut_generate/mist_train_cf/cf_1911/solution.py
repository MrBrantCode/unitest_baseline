"""
QUESTION:
Write a function `calculate_standard_deviation` that calculates the standard deviation of a given set of numbers without using any built-in functions or libraries for calculating standard deviation. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input list. The input list will contain at least 1000 numbers with a maximum value of 10000, and may include negative numbers.
"""

import math

def calculate_standard_deviation(numbers):
    n = len(numbers)
    
    # Calculate the mean
    total = 0
    for num in numbers:
        total += num
    mean = total / n
    
    # Calculate the sum of squared differences
    sum_of_squared_diff = 0
    for num in numbers:
        diff = num - mean
        squared_diff = diff * diff
        sum_of_squared_diff += squared_diff
    
    # Divide by the total number of numbers
    variance = sum_of_squared_diff / n
    
    # Take the square root
    std_deviation = math.sqrt(variance)
    
    return std_deviation