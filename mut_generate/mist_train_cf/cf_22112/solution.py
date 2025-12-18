"""
QUESTION:
Write a function `calculate_statistics(arr)` that calculates the mean, median, and standard deviation from the input array `arr` without using built-in functions or libraries. The function should have a time complexity of O(n) and space complexity of O(1), where n is the number of elements in `arr`. The input array can contain up to 1 million numbers ranging from -10^9 to 10^9, and may be empty or contain duplicate numbers.
"""

def calculate_statistics(arr):
    n = len(arr)
    if n == 0:
        return None, None, None
    
    # Calculate the sum and the number of elements in the array
    total_sum = 0
    for num in arr:
        total_sum += num
    
    # Calculate the mean
    mean = total_sum / n
    
    # Calculate the sum of squares
    sum_of_squares = 0
    for num in arr:
        sum_of_squares += (num - mean) ** 2
    
    # Calculate the variance and standard deviation
    variance = sum_of_squares / n
    standard_deviation = variance ** 0.5
    
    # Sort the array to find the median
    arr.sort()
    
    # Calculate the median
    if n % 2 == 0:
        median = (arr[n // 2 - 1] + arr[n // 2]) / 2
    else:
        median = arr[n // 2]
    
    return mean, median, standard_deviation