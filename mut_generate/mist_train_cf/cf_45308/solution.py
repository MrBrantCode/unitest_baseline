"""
QUESTION:
Write a function `numRollsToTarget(d, f, target)` that calculates the number of potential outcomes modulo `10^9 + 7` that result in the sum of the numbers on the faces of `d` dice, each with `f` faces, being equal to a specific `target`. The function should take three integers as input: `d`, `f`, and `target`, where `1 <= d, f <= 30` and `1 <= target <= 1000`, and return an integer as the result.
"""

def numRollsToTarget(d, f, target):
    MOD = 10**9 + 7
    dp = [[0]*(target+1) for _ in range(d+1)]
    dp[0][0] = 1
    
    for i in range(1, d+1):
        for j in range(1, target+1):
            for k in range(1, min(j, f)+1):
                dp[i][j] = (dp[i][j] + dp[i-1][j-k]) % MOD
    return dp[d][target]