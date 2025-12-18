"""
QUESTION:
Write a function `find_maximum_sum(arr)` that finds the maximum sum for a non-contiguous subarray of a given array, where the array can contain both positive and negative numbers, and the subarray should contain at least two elements. The function should have a time complexity of O(n), where n is the length of the array, and should be able to handle edge cases such as arrays with all negative numbers or arrays with all positive numbers, as well as arrays with both integer and floating-point numbers.
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