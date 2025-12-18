"""
QUESTION:
Implement the `max_subarray_sum` function to find the maximum sum of a subarray in a given array of integers. The function should have a time complexity of O(n) and a space complexity of O(1). It should be able to handle arrays containing both positive and negative integers. If all elements in the array are negative, the function should return the maximum element in the array.
"""

def max_subarray_sum(arr):
    if len(arr) == 0:
        return 0
    
    max_sum = arr[0]
    current_sum = arr[0]
    
    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)
    
    return max_sum