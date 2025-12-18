"""
QUESTION:
Write a function `find_largest_sum` that takes an array of integers as input and returns the maximum sum of a subarray such that no two elements in the subarray are adjacent to each other in the original array.
"""

def find_largest_sum(array: list) -> int:
    n = len(array)
    if n == 1: return array[0]

    dp = [0]*n
    dp[0], dp[1] = array[0], max(array[0], array[1])
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + array[i])
    
    return dp[-1]