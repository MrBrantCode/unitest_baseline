"""
QUESTION:
You are climbing a staircase with `n` steps to reach the top. Each time you can either climb `1` or `2` steps, but you cannot climb two `2` steps consecutively. Write a function named `climbStairs` to calculate the number of distinct ways to climb to the top. The input `n` is an integer that satisfies `1 <= n <= 45`.
"""

def climbStairs(n):
    dp=[[0,0] for _ in range(n+1)]
    dp[0]=[0,0]
    dp[1]=[1,0]
    if n>1:
        dp[2]=[1,1]
    for i in range(3,n+1):
        dp[i][0]=dp[i-1][0]+dp[i-1][1]
        dp[i][1]=dp[i-2][0]
    return sum(dp[n])