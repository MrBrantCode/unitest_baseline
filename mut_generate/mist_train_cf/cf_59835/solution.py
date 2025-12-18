"""
QUESTION:
Write a function `maxSum(arr, k)` that takes an array of integers `arr` and an integer `k` as input and returns the maximum cumulative sum of a sub-array of size `k` within `arr`. The function should return -1 if `k` is greater than the length of `arr`.
"""

def maxSum(arr, k):
    # find the length of the array
    n = len(arr)
    
    # If k is greater than n, return as it's not possible
    if n < k:
        return -1
    
    # Calculate sum of first k elements
    window_sum = sum([arr[i] for i in range(k)])
    max_sum = window_sum
    
    # Compute sums of remaining windows by removing first element and adding next element
    for i in range(n - k):
        window_sum = window_sum - arr[i] + arr[i+k]
        max_sum = max(window_sum, max_sum)
    
    return max_sum