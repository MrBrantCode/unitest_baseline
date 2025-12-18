"""
QUESTION:
Implement a function `calculate_median(arr)` that calculates the median of a given array of integers without using any built-in functions or libraries that directly calculate the median. The function should handle potential edge cases such as empty arrays or arrays containing only negative numbers and ensure that the median is accurate up to 2 decimal places by rounding the result. The input array is not sorted.
"""

def calculate_median(arr):
    # Sort the array in ascending order
    arr = sorted(arr)

    # Determine the length of the sorted array
    length = len(arr)

    # Calculate the median for odd length array
    if length % 2 == 1:
        median = arr[(length - 1) // 2]
    
    # Calculate the median for even length array
    else:
        mid1 = arr[length // 2]
        mid2 = arr[(length // 2) - 1]
        median = (mid1 + mid2) / 2
    
    # Round the median to 2 decimal places
    median = round(median, 2)
    
    return median