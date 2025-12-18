"""
QUESTION:
Write a function `calculate_statistics` that calculates the standard deviation, median, and mean of a given set of numbers. The input array can contain up to 1 million numbers, ranging from -10^9 to 10^9. The function should have a time complexity of O(n) and space complexity of O(1), where n is the number of elements in the input array, and should not use any built-in functions or libraries for calculating statistical measures. The function should also handle duplicate numbers in the input array and correctly handle cases where the input array is empty.
"""

import math

def calculate_statistics(numbers):
    n = len(numbers)
    
    if n == 0:
        return 0, 0, 0
    
    sum_numbers = 0
    sum_squared_numbers = 0
    sorted_numbers = sorted(numbers)
    
    for num in sorted_numbers:
        sum_numbers += num
        sum_squared_numbers += num * num
    
    mean = sum_numbers / n
    
    if n % 2 == 0:
        median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    else:
        median = sorted_numbers[n // 2]
    
    variance = (sum_squared_numbers - (sum_numbers * sum_numbers) / n) / n
    standard_deviation = math.sqrt(variance)
    
    return round(standard_deviation, 2), round(median, 2), round(mean, 2)