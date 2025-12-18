"""
QUESTION:
Implement the function max_subarray_sum that determines the maximum sum of a subarray within the given array, with the constraint that the subarray must contain at least three elements. The function should handle arrays containing negative numbers and achieve this in O(n) time complexity.
"""

def max_subarray_sum(arr):
    if len(arr) == 0:
        return 0
    if len(arr) < 3:
        return max(arr)
    
    max_sum = arr[0]
    current_sum = arr[0]
    
    for i in range(1, len(arr)):
        if current_sum < 0:
            current_sum = 0
        current_sum += arr[i]
        max_sum = max(max_sum, current_sum)
    
    return max_sum