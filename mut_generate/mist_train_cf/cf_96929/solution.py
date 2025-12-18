"""
QUESTION:
Write a function `calculate_statistics` that calculates the mean, median, and standard deviation of a given array of numbers. The input array can contain up to 1 million numbers ranging from -10^9 to 10^9. The solution should have a time complexity of O(n) and space complexity of O(1), where n is the number of elements in the input array. The function should handle duplicate numbers and correctly handle empty input arrays. Do not use built-in functions or libraries for calculating statistical measures.
"""

import math

def calculate_statistics(arr):
    n = len(arr)
    if n == 0:
        return None, None, None
    
    # Calculate the sum and the number of elements in the array
    total_sum = 0
    num_elements = 0
    for num in arr:
        total_sum += num
        num_elements += 1
    
    # Calculate the mean
    mean = total_sum / num_elements
    
    # Calculate the sum of squares
    sum_of_squares = 0
    for num in arr:
        sum_of_squares += (num - mean) ** 2
    
    # Calculate the variance and standard deviation
    variance = sum_of_squares / num_elements
    standard_deviation = math.sqrt(variance)
    
    # Sort the array to find the median
    arr.sort()
    
    # Calculate the median
    if num_elements % 2 == 0:
        median = (arr[num_elements // 2 - 1] + arr[num_elements // 2]) / 2
    else:
        median = arr[num_elements // 2]
    
    return mean, median, standard_deviation