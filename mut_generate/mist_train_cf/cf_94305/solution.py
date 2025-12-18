"""
QUESTION:
Implement the `longest_increasing_subsequence` function, which takes as input an array `arr` of distinct integers greater than 0 and returns the length of the longest increasing subsequence. The length of the array should not exceed 10^6. The solution should have a time complexity of O(n log n) and should be implemented using dynamic programming.
"""

def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)