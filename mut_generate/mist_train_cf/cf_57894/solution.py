"""
QUESTION:
Write a function named `find_max_sum` that takes an array of integers as input and returns the maximum sum of four non-adjacent numbers in the array. The function should not use any sorting algorithm and should work for arrays containing both positive and negative numbers. If the array has four or fewer elements, the function should return the sum of all elements in the array.
"""

def find_max_sum(arr):
    if len(arr) < 4:
        return sum(arr)

    dp = [0]*4 + arr

    for i in range(4, len(dp)):
        dp[i] = max(dp[i-4]+arr[i-4], dp[i-1])

    return dp[-1]