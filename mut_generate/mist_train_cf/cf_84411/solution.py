"""
QUESTION:
Given a one-dimensional array and a positive integer k, write a function `maxSum(arr, k)` to find the maximum sum of a contiguous subarray of size k within the given array. If the array length is less than k, return -1.
"""

def maxSum(arr, k):
    if len(arr) < k:  
        return -1     

    curSum = sum(arr[:k])
    maxSum = curSum  

    for i in range(k, len(arr)):
        curSum = curSum - arr[i-k] + arr[i]
        maxSum = max(maxSum, curSum)
    return maxSum