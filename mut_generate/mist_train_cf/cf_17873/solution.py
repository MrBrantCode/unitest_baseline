"""
QUESTION:
Implement a function `maximum_sum(arr, m)` that calculates the maximum sum of `m` consecutive values in a given array `arr`. If the array contains less than `m` elements, return the smallest possible value. If there are multiple subsequences with the same maximum sum, return the one with the latest starting index. The array may contain negative numbers, non-integer values, and duplicate values.
"""

def maximum_sum(arr, m):
    if len(arr) < m:
        return float('-inf')
    
    maxSum = float('-inf')
    currentSum = sum(arr[:m])
    maxSum = currentSum
    
    for i in range(m, len(arr)):
        currentSum = currentSum - arr[i - m] + arr[i]
        maxSum = max(maxSum, currentSum)
    
    return maxSum