"""
QUESTION:
Implement the `max_subarray_sum` function, which takes a list of integers as input and returns the maximum sum of a contiguous subarray. The function should handle cases where the input list is empty.
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