"""
QUESTION:
Write a function `getMaxSum(arr)` that finds the two numbers in a given array that have the largest sum. The function should return the largest sum. The array contains distinct integers and has at least two elements.
"""

def get_max_sum(arr):
    maxSum = -float('inf')
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            maxSum = max(maxSum, arr[i] + arr[j])
    return maxSum