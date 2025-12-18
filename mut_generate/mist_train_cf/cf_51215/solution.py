"""
QUESTION:
Write a function `max_sum_subarray(arr, k, m)` that takes an array `arr`, an integer `k`, and an integer `m` as input, and returns the maximum sum of a subarray of length `m` in `arr` that is less than `k`. If no such subarray exists, return `None`.
"""

def max_sum_subarray(arr, k, m):
    n = len(arr)
    max_sum = float('-inf')
    for i in range(n - m + 1):  
        cur_sum = sum(arr[i:i + m])  
        if cur_sum < k and cur_sum > max_sum:  
            max_sum = cur_sum
    if max_sum == float('-inf'):  
        return None
    return max_sum