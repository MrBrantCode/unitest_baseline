"""
QUESTION:
Write a function named `find_maximum_sum` that takes an array of integers or floating-point numbers as input and returns the maximum sum of a non-contiguous subarray containing at least two elements. The function should have a time complexity of O(n), where n is the length of the array, and should be able to handle edge cases such as empty arrays, arrays with all negative numbers, and arrays with all positive numbers. The function should also handle both integer and floating-point numbers and use minimal memory.
"""

def find_maximum_sum(arr):
    # If the array contains less than 2 elements, return 0 as there can't be a valid subarray
    if len(arr) < 2:
        return 0

    # Initialize variables to store the maximum sum of subarrays ending at the current index
    include_current = max(0, arr[0])
    exclude_current = 0

    # Iterate over the array, starting from the second element
    for i in range(1, len(arr)):
        # Calculate the maximum sum of subarrays ending at the current index
        new_include_current = max(exclude_current + arr[i], include_current)
        exclude_current = include_current
        include_current = new_include_current

    # Return the maximum sum
    return max(include_current, exclude_current)