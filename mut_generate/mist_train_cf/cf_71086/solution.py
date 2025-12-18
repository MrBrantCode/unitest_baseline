"""
QUESTION:
Given a positive integer `n`, implement a function `getMoneyAmount(n)` to calculate the minimum amount of money needed to guarantee a win in a guessing game where you guess a number between `1` and `n`. After each wrong guess, the number is changed to another number within the remaining range, and you pay the guessed number as a penalty. The function should return the minimum cost for a given `n`, where `1 <= n <= 200`.
"""

def getMoneyAmount(n):
    dp = [[0] * (n+1) for _ in range(n+1)]
    for j in range(2, n+1):
        for i in range(j-1, 0, -1):
            global_min = float('inf')
            for x in range(i+1, j):
                local_max = x + max(dp[i][x-1], dp[x+1][j])
                global_min = min(global_min, local_max)
            dp[i][j] = i if i + 1 == j else global_min
    return dp[1][n]