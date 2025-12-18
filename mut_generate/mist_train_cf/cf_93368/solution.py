"""
QUESTION:
Implement a function `max_subarray_sum` that finds the maximum sum of a subarray within a given array of integers. The function should take an array of integers as input and return the maximum sum found. The function must use dynamic programming to achieve this, and the array can contain both positive and negative integers.
"""

def max_subarray_sum(arr):
    n = len(arr)
    
    if n == 0:
        return 0
    
    # Initialize variables
    max_sum = arr[0]
    current_sum = arr[0]
    
    # Iterate through the array
    for i in range(1, n):
        # Update current_sum by adding the current element to it
        current_sum = max(arr[i], current_sum + arr[i])
        
        # Update max_sum if current_sum is greater
        max_sum = max(max_sum, current_sum)
    
    return max_sum