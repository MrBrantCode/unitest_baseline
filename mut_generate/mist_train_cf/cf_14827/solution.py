"""
QUESTION:
Design a function `calculate_standard_deviation` to calculate the standard deviation of a given list of numbers. The list may contain duplicates and negative numbers. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the number of elements in the list.
"""

import math

def calculate_standard_deviation(data):
    n = len(data)
    if n < 2:
        return 0
    
    sum_x = 0
    sum_x_squared = 0
    for x in data:
        sum_x += x
        sum_x_squared += x ** 2
    
    mean = sum_x / n
    variance = (sum_x_squared / n) - (mean ** 2)
    standard_deviation = math.sqrt(variance)
    
    return standard_deviation