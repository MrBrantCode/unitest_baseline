"""
QUESTION:
Implement a function `maxSumSubarray` that takes an array of integers and a window size as input and returns the maximum sum of a subarray of that size. The function should handle cases where the window size is larger than the array size by returning 0. The input array will contain only integers, and the window size will be a positive integer.
"""

from typing import List

def maxSumSubarray(arr: List[int], windowSize: int) -> int:
    if windowSize > len(arr):
        return 0  

    maxSum = float('-inf')
    windowSum = 0

    for i in range(windowSize):
        windowSum += arr[i]

    maxSum = max(maxSum, windowSum)

    for i in range(windowSize, len(arr)):
        windowSum = windowSum - arr[i - windowSize] + arr[i]
        maxSum = max(maxSum, windowSum)

    return maxSum