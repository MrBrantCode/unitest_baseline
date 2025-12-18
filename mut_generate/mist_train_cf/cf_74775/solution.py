"""
QUESTION:
Write a function `longest_ascending_subarray` that finds the length of the longest ascending subarray within a given array. The function should handle edge cases and have a time complexity of O(n) and a space complexity of O(n), where n is the length of the array.
"""

def longest_ascending_subarray(arr):
    if not arr: 
        return 0

    dp = [1]*len(arr) 
    max_length = 1 

    for i in range(1, len(arr)):

        if arr[i] > arr[i-1]:
            dp[i] = dp[i-1] + 1

        max_length = max(max_length, dp[i])

    return max_length