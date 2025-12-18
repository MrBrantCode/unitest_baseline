"""
QUESTION:
Write a function named `max_subarray_sum` that takes an array of integers as input and returns the maximum sum of a subarray within the array. The subarray must consist of consecutive elements from the original array. The function must have a time complexity of O(n), where n is the length of the input array, and cannot use any built-in functions or libraries.
"""

def max_subarray_sum(arr):
    if not arr:
        return 0
    
    max_sum = arr[0]
    current_sum = arr[0]
    
    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)
    
    return max_sum