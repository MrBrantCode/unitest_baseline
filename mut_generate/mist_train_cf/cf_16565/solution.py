"""
QUESTION:
Implement the function longest_increasing_subsequence(arr) to find the length of the longest increasing subsequence in the given array arr, where each element is distinct and greater than 0. The function should have a time complexity of O(n log n) and use dynamic programming. The length of the array should not exceed 10^6.
"""

def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)