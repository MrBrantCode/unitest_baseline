"""
QUESTION:
Write a function `maxSubarraySum` that takes an array of integers as input and returns the maximum sum of a subarray within the given array, with the constraint that the subarray must contain at least two elements. If the array has less than two elements, return `None`.
"""

def maxSubarraySum(arr):
    if len(arr) < 2:
        return None
    
    maxSoFar = arr[0]
    maxEndingHere = arr[0]
    
    for i in range(1, len(arr)):
        maxEndingHere = max(arr[i], maxEndingHere + arr[i])
        maxSoFar = max(maxSoFar, maxEndingHere)
    
    return maxSoFar