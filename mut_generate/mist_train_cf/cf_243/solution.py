"""
QUESTION:
Write a function `max_subarray_sum` that finds the maximum subarray sum in a circular array. The function must have a time complexity of O(n) and space complexity of O(1), without using any extra data structures. The input is an array of integers, and the output is the maximum subarray sum.
"""

def maxSubArraySum(a):
    n = len(a)
    
    # Case 1: Maximum subarray sum in a non-circular array
    max_sum = a[0]
    current_sum = a[0]
    
    for i in range(1, n):
        current_sum = max(a[i], current_sum + a[i])
        max_sum = max(max_sum, current_sum)
    
    # Case 2: Maximum subarray sum in a circular array
    total_sum = sum(a)
    
    # Invert the sign of all elements in the array
    for i in range(n):
        a[i] = -a[i]
    
    # Find the minimum subarray sum in the inverted array
    min_sum = a[0]
    current_sum = a[0]
    
    for i in range(1, n):
        current_sum = min(a[i], current_sum + a[i])
        min_sum = min(min_sum, current_sum)
    
    # Maximum subarray sum in a circular array is the difference between
    # the total sum and the minimum subarray sum in the inverted array
    circular_max_sum = total_sum + min_sum
    
    # Return the maximum of the two cases
    return max(max_sum, circular_max_sum)