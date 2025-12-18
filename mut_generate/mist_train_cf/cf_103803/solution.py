"""
QUESTION:
Create a function `calculate_statistics` that takes a list of numbers as input and returns the standard deviation, median, and mean of the numbers. The function should have a time complexity of O(n), where n is the number of elements in the input list. The input list can contain up to 1 million numbers.
"""

import math

def calculate_statistics(numbers):
    n = len(numbers)
    if n == 0:
        return None, None, None
    
    # Calculate mean
    total = sum(numbers)
    mean = total / n
    
    # Calculate variance
    variance = sum((x - mean) ** 2 for x in numbers) / n
    
    # Calculate standard deviation
    std_deviation = math.sqrt(variance)
    
    # Calculate median
    sorted_numbers = sorted(numbers)
    middle_index = n // 2
    if n % 2 == 0:
        median = (sorted_numbers[middle_index - 1] + sorted_numbers[middle_index]) / 2
    else:
        median = sorted_numbers[middle_index]
    
    return std_deviation, median, mean