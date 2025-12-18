"""
QUESTION:
Write a function `new21Game(N: int, K: int, W: int) -> float` that calculates the probability that the total points of Alice and Bob will be `N` or less in a game where Alice and Bob draw numbers from the range `[1, W]` until they accumulate `K` or more points. Assume `0 <= K <= N <= 20000` and `1 <= W <= 10000`. The answer will be considered correct if it is within `10^-5` of the accurate answer.
"""

def new21Game(N: int, K: int, W: int) -> float:
    if K == 0 or N >= K + W: return 1.0
    dp = [0.0] * (N + 1)
    dp[0] = 1.0
    Wsum = 1.0
    res = 0.0
    for i in range(1, N + 1):
        dp[i] = Wsum / W
        if i < K: 
            Wsum += dp[i]
        else: 
            res += dp[i]
        if i - W >= 0:
            Wsum -= dp[i - W]
    return res