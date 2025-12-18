"""
QUESTION:
Given `N`, `K`, and `W` integers, return the probability that Alice's total points will be `N` or less in a game where she draws numbers from the range `[1, W]` as long as her points are less than `K`. The game concludes when Alice accumulates `K` or more points. The constraints are `0 <= K <= N <= 10000` and `1 <= W <= 10000`. The answer should be accurate within `10^-5`. Implement a function `new21Game(N: int, K: int, W: int) -> float` to solve this problem.
"""

def new21Game(N: int, K: int, W: int) -> float:
    if K == 0 or N >= K + W: 
        return 1
    dp = [0.0] * (N+1)
    dp[0] = 1
    Wsum = 1.0
    res = 0
    for i in range(1, N+1):
        dp[i] = Wsum / W
        if i < K:
            Wsum += dp[i]
        else:
            res += dp[i]
        if i-W >= 0:
            Wsum -= dp[i-W]
    return res