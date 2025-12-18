"""
QUESTION:
Create a function `longestAscendingSubsequence(arr)` that takes an array of integers as input and returns the length of the longest increasing subsequence (LIS) within the array. The function should use dynamic programming and return the maximum length of the LIS. The input array is 0-indexed.
"""

def longestAscendingSubsequence(arr):
    n = len(arr)
  
    # Initialize Longest Increasing Subsequence values for all indexes
    lis = [1]*n
  
    # Compute optimized LIS values in bottom up manner
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i]< lis[j] + 1:
                lis[i] = lis[j]+1
  
    # Initialize maximum to 0 to get the maximum of all LIS
    maximum = 0
  
    # Pick the maximum of all LIS values
    for i in range(len(lis)):
        maximum = max(maximum, lis[i])
  
    return maximum