"""
QUESTION:
Create a function `longest_common_subsequence(x, y)` that takes two strings `x` and `y` as input and returns their longest common subsequence. If no common subsequence exists, return '-1'. The function must also favor lexicographically smallest common subsequence, by preferring deletion from the first sequence `x` over the second sequence `y`.
"""

def longest_common_subsequence(x, y):
    m = len(x)
    n = len(y)

    dp = [[0]*(n+1) for i in range(m+1)]
    dir_ = [[0]*(n+1) for i in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0 :
                dp[i][j] = 0
            elif x[i-1] == y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                dir_[i][j] = 'diagonal'
            elif dp[i-1][j] > dp[i][j-1]: 
                dp[i][j] = dp[i-1][j]
                dir_[i][j] = 'up'
            else:
                dp[i][j] = dp[i][j-1]
                dir_[i][j] = 'left'

    lcs = ""
    while m > 0 and n > 0:
        if dir_[m][n] == 'diagonal':
            lcs += x[m-1]
            m -= 1
            n -= 1
        elif dir_[m][n] == 'up':
            m -= 1
        else:
            n -= 1

    if len(lcs) > 0:
        return lcs[::-1]
    else:
        return '-1'