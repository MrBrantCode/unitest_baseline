"""
QUESTION:
Write a function `max_sum_no_adjacent` that takes an array of integers as input and returns the maximum sum achievable by incorporating distinct elements from the array, such that two utilized elements never share a common positional index. The function should be able to handle arrays of any length, including empty arrays and arrays with only one or two elements.
"""

def max_sum_no_adjacent(arr):
    if not arr:
        return 0
    
    elif len(arr) <= 2:
        return max(arr)
    
    else:
        dp = [0] * len(arr)
        dp[0] = arr[0]
        dp[1] = max(arr[0], arr[1])

        for i in range(2, len(arr)):
            dp[i] = max(dp[i - 2] + arr[i], dp[i - 1])
                
        return dp[-1]