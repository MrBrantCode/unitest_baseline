"""
QUESTION:
Write a function `max_cumulative_value(arr)` that computes the maximum cumulative value from the elements in the input array `arr` such that no two selected elements are directly neighboring each other. The function should return the maximum cumulative value and must run in linear time complexity with respect to the length of the input array.
"""

def max_cumulative_value(arr):
    # If input array is empty
    if not arr:
        return 0

    # If input array contains only one element
    if len(arr) == 1:
        return arr[0]

    # Initialize the array to store the maximum cumulative value
    dp = [0] * len(arr)
    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])

    # Fill dp array using bottom-up dynamic programming approach
    for i in range(2, len(arr)):
        dp[i] = max(dp[i-1], dp[i-2] + arr[i])

    # Return the maximum cumulative value
    return dp[-1]