"""
QUESTION:
Given a list of stone piles `stones` and an integer `K`, write a function `mergeStones` that returns the minimum cost to merge all stone piles into a single pile. The cost of merging exactly `K` consecutive piles into a single pile is the sum of stones in these `K` piles. If it's impossible to merge all stone piles into a single pile, return `-1`. 

Restrictions: `1 <= len(stones) <= 30`, `2 <= K <= 30`, `1 <= stones[i] <= 100`.
"""

def mergeStones(stones, K: int) -> int:
    N = len(stones)
    prefix = [0] * (N+1)
    inf = float('inf')
    for i in range(N):
        prefix[i+1] = prefix[i] + stones[i]

    dp = [[[inf] * (K+1) for _ in range(N+1)] for _ in range(N+1)]
    for i in range(1, N+1):
        dp[i][i][1] = 0

    for len_ in range(2, N+1):
        for i in range(1, N+2-len_):
            j = i+len_-1
            for k in range(2, K+1):
                dp[i][j][k] = min(dp[i][mid][1] + dp[mid+1][j][k-1] for mid in range(i, j, K-1))
            if (j - i) % (K-1) == 0:
                dp[i][j][1] = dp[i][j][K] + prefix[j] - prefix[i-1]

    return -1 if dp[1][N][1] == inf else dp[1][N][1]