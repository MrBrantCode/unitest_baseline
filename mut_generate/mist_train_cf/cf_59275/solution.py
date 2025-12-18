"""
QUESTION:
Implement a function `longest_subsequence(arr)` that takes an array of integers as input and returns the length of the longest increasing subsequence. The subsequence should be strictly increasing, meaning each element is greater than its previous element. The function should have a time complexity of O(n^2) or better.
"""

def longest_subsequence(arr):
    n = len(arr)

    # Initialize Longest Increasing Subsequence values for all indexes
    lis = [1]*n
    
    # Compute optimized LIS values in bottom up manner
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j]+1

    # Initialize maximum to 0 to get the maximum of all LIS
    maximum = 0

    # Pick maximum of all LIS values
    for i in range(len(lis)):
        maximum = max(maximum, lis[i])

    return maximum