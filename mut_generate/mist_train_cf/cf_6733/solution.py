"""
QUESTION:
Write a function `calculate_standard_deviation` that takes a list of numbers as input and returns the standard deviation of the positive values in the list, excluding negative values. The function should consider only the positive values in the range of 1 to 1000, and the standard deviation should be a floating-point number rounded to 2 decimal places and then rounded to the nearest even number.
"""

import math

def calculate_standard_deviation(numbers):
    # Filter out negative values and values outside the range of 1 to 1000
    positive_numbers = [num for num in numbers if 1 <= num <= 1000 and num > 0]
    
    # Calculate the mean of the positive numbers
    mean = sum(positive_numbers) / len(positive_numbers)
    
    # Calculate the squared differences from the mean
    squared_differences = [(num - mean) ** 2 for num in positive_numbers]
    
    # Calculate the variance as the average of the squared differences
    variance = sum(squared_differences) / len(squared_differences)
    
    # Calculate the standard deviation as the square root of the variance
    standard_deviation = math.sqrt(variance)
    
    # Round the standard deviation to 2 decimal places
    standard_deviation_rounded = round(standard_deviation, 2)
    
    # Round the standard deviation to the nearest even number
    standard_deviation_rounded_even = round(standard_deviation_rounded / 2) * 2
    
    return standard_deviation_rounded_even