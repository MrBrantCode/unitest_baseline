"""
QUESTION:
Write a function `maxSideJumps` that takes a list of integers `rewards` representing rewards on a 3-lane road of length `n` and returns the maximum number of side jumps a frog can make to collect as many rewards as possible. The frog starts at point `0` in the second lane and can only travel to point `i + 1` on the same lane if there is a reward on the lane at point `i + 1`. The frog can also perform a side jump to another lane at the same point if there is a reward on the new lane. The function should have a time complexity of O(n) and a space complexity of O(n).
"""

def maxSideJumps(rewards):
    n = len(rewards)
    dp = [[float('inf')] * 3 for _ in range(n)]
    dp[0][1] = 0

    for i in range(1, n):
        for j in range(3):
            if rewards[i][j] == 1:
                dp[i][j] = min(dp[i][j], dp[i-1][j])
                for k in range(3):
                    if k != j:
                        dp[i][j] = min(dp[i][j], dp[i-1][k] + 1)

    return min(dp[-1])