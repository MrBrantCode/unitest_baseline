"""
QUESTION:
Given a table of n rows and m columns, each cell containing a positive integer, write a function `maximum_sum(table)` to find the maximum sum of integers that can be obtained by selecting one cell from each row, with the selected cells being from different columns. The function should run within a time complexity of O(nlogn).
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
                dp[i][j] = max_val + table[i][j]
    
    return max(dp[n-1])