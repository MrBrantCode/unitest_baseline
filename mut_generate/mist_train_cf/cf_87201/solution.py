"""
QUESTION:
Calculate the standard deviation of a given set of numbers. The function name should be `calculate_standard_deviation` and it should take one parameter, `numbers`, which is a list of numbers. The solution should have a time complexity of O(n) and a space complexity of O(1), where n is the number of elements in the list. The implementation should not use any built-in functions or libraries for calculating standard deviation. The input list will contain at least 1000 numbers, each with a maximum value of 10000, and may include negative numbers.
"""

import math

def calculate_standard_deviation(numbers):
    n = len(numbers)
    
    # Step 1: Calculate the mean
    total = 0
    for num in numbers:
        total += num
    mean = total / n
    
    # Step 2: Calculate the sum of squared differences
    sum_of_squared_diff = 0
    for num in numbers:
        diff = num - mean
        squared_diff = diff * diff
        sum_of_squared_diff += squared_diff
    
    # Step 3: Divide by the total number of numbers
    variance = sum_of_squared_diff / n
    
    # Step 4: Take the square root
    std_deviation = math.sqrt(variance)
    
    return std_deviation