"""
QUESTION:
Write a function named `calculate_median` that takes an array of integers as input and returns the median of the array. The array may contain both positive and negative integers. The function should handle both odd and even length arrays.
"""

def calculate_median(arr):
    sorted_arr = sorted(arr)  # Sort the array in ascending order
    n = len(sorted_arr)
    if n % 2 == 0:
        # If the array length is even, average the middle two numbers
        median = (sorted_arr[n//2-1] + sorted_arr[n//2]) / 2
    else:
        # If the array length is odd, take the middle number
        median = sorted_arr[n//2]
    return median