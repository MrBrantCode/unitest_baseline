"""
QUESTION:
Find the maximum sum of any subarray with a length of at least 2 in a given array of integers. The array can contain both positive and negative integers, and the maximum sum can be negative if all integers in the array are negative. Implement a function `maximum_subarray_sum(arr)` to solve this problem.
"""

def maximum_subarray_sum(arr):
    n = len(arr)
    maxSum = arr[0]
    currentSum = arr[0]

    for i in range(1, n):
        currentSum += arr[i]
        
        if currentSum > maxSum:
            maxSum = currentSum

        if currentSum < 0:
            currentSum = 0

    return maxSum