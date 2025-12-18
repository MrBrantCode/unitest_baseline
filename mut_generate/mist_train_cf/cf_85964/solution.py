"""
QUESTION:
Implement a function `calculateMinimumHP(dungeon)` to calculate the minimum initial health points required for a knight to rescue a princess in a 3D dungeon. The dungeon is represented as a 3D array `dungeon` where `m == dungeon.length`, `n == dungeon[i].length`, `o == dungeon[i][j].length`, `1 <= m, n, o <= 100`, and `-1000 <= dungeon[i][j][k] <= 1000`. The function should return the minimum initial health points required for the knight to reach the princess.
"""

def calculateMinimumHP(dungeon):
    m, n, o = len(dungeon), len(dungeon[0]), len(dungeon[0][0])
    dp = [[[0] * (o + 1) for _ in range(n + 1)] for _ in range(m + 1)]
    dp[m][n - 1][o - 1] = dp[m - 1][n][o - 1] = dp[m - 1][n - 1][o] = 1
    for i in reversed(range(m)):
        for j in reversed(range(n)):
            for k in reversed(range(o)):
                dp[i][j][k] = max(min(dp[i+1][j][k], dp[i][j+1][k], dp[i][j][k+1]) - dungeon[i][j][k], 1)
    return dp[0][0][0]