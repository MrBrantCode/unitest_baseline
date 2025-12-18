"""
QUESTION:
The function count_ways(n, k) should calculate the number of ways an automaton can return to its initial point after n movements, where each movement is either +1 (anticlockwise) or -1 (clockwise) and the sum of all movements equals k. The automaton starts facing north and can move in one-fifth circular trajectories, with the liberty to select either a clockwise or an anticlockwise trajectory for each progression, but devoid of any stationary rotation. The function should return the total count of such sequences.
"""

def entrance(n, k):
    dp = [[0]*(2*n+1) for _ in range(n+1)]
    dp[0][n] = 1
    for i in range(1, n+1):
        for j in range(2*n+1):
            if j-1 >= 0:
                dp[i][j] += dp[i-1][j-1]
            if j+1 <= 2*n:
                dp[i][j] += dp[i-1][j+1]
    return dp[n][n+k]