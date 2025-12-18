"""
QUESTION:
Write a function `max_sum` that calculates the maximum sum of `m` consecutive values in an array. The array can contain negative numbers and may be empty or contain less than `m` elements. In such cases, the function should return 0. If multiple subsequences have the same maximum sum, return the one with the earliest starting index. The function should take two parameters: an array `arr` and an integer `m`.
"""

def max_sum(arr, m):
    if len(arr) < m:
        return 0
    
    start = 0
    end = 0
    maxSum = 0
    windowSum = 0
    
    while end < len(arr):
        windowSum += arr[end]
        
        if end - start + 1 == m:
            maxSum = max(maxSum, windowSum)
            windowSum -= arr[start]
            start += 1
        
        end += 1
    
    return maxSum