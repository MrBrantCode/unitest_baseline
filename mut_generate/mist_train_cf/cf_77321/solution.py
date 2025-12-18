"""
QUESTION:
Write a function named `minimumRemovals` that takes an array of integers as input and returns the minimum number of operations required to completely empty the array. The array can be emptied by identifying a subarray that forms a palindrome and eliminating it in a single operation. The subarray must comprise at least 3 elements. The length of the array is between 3 and 100, and each element is between 1 and 20.
"""

def minimumRemovals(arr):
    n = len(arr)
    dp = [[0] * n for _ in range(n)]
    for length in range(1, n+1):
        for i in range(n - length + 1):
            j = i + length - 1
            if length == 1:
                dp[i][j] = 1
            elif length == 2:
                dp[i][j] = 1 if arr[i] == arr[j] else 2
            else:
                if arr[i] == arr[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = min(dp[i][k] + dp[k + 1][j] for k in range(i, j))
    return dp[0][n - 1]