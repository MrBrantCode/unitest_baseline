"""
QUESTION:
Write a function `maximum_sum_subsequence(arr)` that returns the maximum sum of a subsequence in the given array `arr`. The subsequence can be any length, but it must be non-empty. If the array contains only negative numbers, return the smallest negative number. If the array contains both positive and negative numbers, return the sum of the subsequence that maximizes the sum. If multiple subsequences have the same maximum sum, return the sum of the subsequence with the smallest length.
"""

def maximum_sum_subsequence(arr):
    max_sum = arr[0]
    current_sum = arr[0]
    
    for i in range(1, len(arr)):
        current_sum += arr[i]
        
        if current_sum > max_sum:
            max_sum = current_sum
        
        if current_sum < 0:
            current_sum = 0
    
    if max_sum < 0:
        return max(arr)
    else:
        return max_sum