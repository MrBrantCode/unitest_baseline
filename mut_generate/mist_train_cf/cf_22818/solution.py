"""
QUESTION:
Implement a function `max_subarray_sum` that takes an array of integers as input and returns the maximum sum of a subarray. The function should have a time complexity of O(n) and a space complexity of O(1), and it should be able to handle arrays containing both positive and negative integers.
"""

def max_subarray_sum(arr):
    maxSoFar = arr[0]
    maxEndingHere = arr[0]
    
    for i in range(1, len(arr)):
        maxEndingHere = max(arr[i], maxEndingHere + arr[i])
        maxSoFar = max(maxSoFar, maxEndingHere)
        
    return maxSoFar