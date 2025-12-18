"""
QUESTION:
Write a function named `calculate_statistics` that takes a list of numbers as input and returns the standard deviation, median, and mean. The function should have a time complexity of O(n), where n is the number of elements in the input array. The input array can contain up to 1 million numbers.
"""

import math

def calculate_statistics(numbers):
    n = len(numbers)
    if n == 0:
        return None, None, None
    
    total = sum(numbers)
    mean = total / n
    
    variance = sum((x - mean) ** 2 for x in numbers) / n
    std_deviation = math.sqrt(variance)
    
    sorted_numbers = sorted(numbers)
    middle_index = n // 2
    median = (sorted_numbers[middle_index - 1] + sorted_numbers[middle_index]) / 2 if n % 2 == 0 else sorted_numbers[middle_index]
    
    return std_deviation, median, mean