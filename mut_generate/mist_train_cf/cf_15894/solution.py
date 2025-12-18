"""
QUESTION:
Write a function `maximum_subarray_sum(arr, k)` that calculates the maximum sum of elements of a given subarray of length k in an array of integers. The function should not use any built-in functions or methods for calculating the sum of the subarray. It should also not store intermediate sums or the final maximum sum in any variable other than a single accumulator. The function should return the maximum sum of elements of the subarray of length k.
"""

def maximum_subarray_sum(arr, k):
    maxSum = currentSum = sum(arr[:k])  
    for i in range(k, len(arr)):
        currentSum += arr[i] - arr[i - k]  
        maxSum = max(maxSum, currentSum)  
    return maxSum