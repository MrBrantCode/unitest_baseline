"""
QUESTION:
Write a function `max_sum_subarray(arr, k, m)` that takes an array `arr` of integers, a target sum `k`, and a minimum subarray length `m` as input, and returns the maximum sum of a subarray with length at least `m` that is less than `k` and contains at least one negative number.
"""

def max_sum_subarray(arr, k, m):
    n = len(arr)
    max_sum = float('-inf')
    left = 0
    right = m - 1
    
    while right < n:
        current_sum = sum(arr[left:right+1])
        if current_sum < k and any(num < 0 for num in arr[left:right+1]):
            max_sum = max(max_sum, current_sum)
        left += 1
        right += 1
    
    return max_sum