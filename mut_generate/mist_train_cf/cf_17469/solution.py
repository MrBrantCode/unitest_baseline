"""
QUESTION:
Write a function `maxSubarraySum(arr, k)` that takes an array of integers `arr` and an integer `k` as input, and returns the length of the longest subarray with a sum less than or equal to `k`. If there are multiple subarrays with the maximum sum, return the length of the longest subarray among them.
"""

def maxSubarraySum(arr, k):
    """
    Returns the length of the longest subarray with a sum less than or equal to k.
    
    Parameters:
    arr (list): A list of integers
    k (int): The maximum sum of the subarray
    
    Returns:
    int: The length of the longest subarray with a sum less than or equal to k
    """
    n = len(arr)
    maxSum = float('-inf')
    maxLength = 0
    for i in range(n):
        for j in range(i, n):
            subarraySum = sum(arr[i:j+1])
            subarrayLength = j - i + 1
            if subarraySum <= k:
                if subarraySum > maxSum or (subarraySum == maxSum and subarrayLength > maxLength):
                    maxSum = subarraySum
                    maxLength = subarrayLength
    return maxLength