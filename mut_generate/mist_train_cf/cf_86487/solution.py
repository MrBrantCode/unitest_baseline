"""
QUESTION:
Design a function `find_median(arr)` that calculates the median of an array of integers and floating-point numbers with the following restrictions: 

The function should handle arrays with duplicate elements, negative numbers, zero, non-numeric elements, and NaN elements (which are considered as positive infinity). It should return the median as a floating-point number with precision up to two decimal places. The function should have a time complexity of O(n log n) and a space complexity of O(1) by modifying the input array in place, without using built-in median calculation functions or libraries.
"""

import math

def find_median(arr):
    # Remove non-numeric elements
    arr = [x for x in arr if isinstance(x, (int, float))]

    # Replace NaN with positive infinity
    arr = [float('inf') if isinstance(x, float) and math.isnan(x) else x for x in arr]

    # Sort the array
    arr.sort()

    # Calculate the length of the array
    n = len(arr)

    # Calculate the median
    if n % 2 == 1:
        median = arr[n // 2]
    else:
        median = (arr[n // 2 - 1] + arr[n // 2]) / 2

    # Round the median to two decimal places
    median = round(median, 2)

    # Return the median
    return median