"""
QUESTION:
Given a table of n rows and m columns with each cell containing a positive integer, write a function `maximum_sum` that finds the maximum sum of integers by selecting one cell from each row and ensuring the selected cells are from different columns, within a time complexity of O(nlogn).
"""

def maximum_sum(table):
    n, m = len(table), len(table[0])
    dp = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if i == 0:
                dp[i][j] = table[i][j]
            else:
                max_val = float('-inf')
                for k in range(m):
                    if k != j:
                        max_val = max(max_val, dp[i-1][k])
                dp[i][j] = table[i][j] + max_val

    return max(dp[-1]) 