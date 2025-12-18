"""
QUESTION:
Write a function `max_subarray_sum` that finds the maximum contiguous subarray sum in a given array. The function must have a time complexity of O(n) and a space complexity of O(1), where n is the number of elements in the array. The input array may be empty. If the array is empty, the function should return 0.
"""

def max_subarray_sum(arr):
    if not arr:
        return 0
    
    max_sum = arr[0]
    curr_sum = arr[0]
    
    for i in range(1, len(arr)):
        curr_sum = max(arr[i], curr_sum + arr[i])
        max_sum = max(max_sum, curr_sum)
    
    return max_sum