"""
QUESTION:
Implement a function named `max_subarray_sum` that takes an array of integers as input and returns the maximum sum of a contiguous subarray. The input array can be empty, and if so, the function should return 0. The function should have a time complexity of O(n), where n is the number of elements in the array.
"""

def max_subarray_sum(arr):
    if len(arr) == 0:
        return 0
    
    max_sum = arr[0]  # initialize the maximum subarray sum to be the first element
    curr_sum = arr[0]  # initialize the current subarray sum to be the first element
    
    for i in range(1, len(arr)):
        curr_sum = max(arr[i], curr_sum + arr[i])  # update the current subarray sum by either adding the current element or starting a new subarray
        max_sum = max(max_sum, curr_sum)  # update the maximum subarray sum if the current subarray sum is greater
    
    return max_sum