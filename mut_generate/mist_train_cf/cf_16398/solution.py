"""
QUESTION:
Write a function named 'calculate_standard_deviation' that calculates the standard deviation of an array, excluding any negative numbers and zero. The function should take an array of numbers as input, round the standard deviation to two decimal places, and return the result.
"""

import math

def calculate_standard_deviation(arr):
    # Filter out the negative numbers and zeros from the array
    filtered_arr = [num for num in arr if num > 0]
    
    # Calculate the mean of the filtered array
    mean = sum(filtered_arr) / len(filtered_arr)
    
    # Calculate the variance of the filtered array
    variance = sum((num - mean) ** 2 for num in filtered_arr) / len(filtered_arr)
    
    # Calculate the standard deviation of the filtered array
    std_deviation = math.sqrt(variance)
    
    # Round the standard deviation to two decimal places
    std_deviation = round(std_deviation, 2)
    
    return std_deviation