"""
QUESTION:
Function `videoStitching(clips, costs, T)` 

Given a series of video clips with costs, return the minimum cost and the specific clips used to cover the entire sporting event `[0, T]`. The clips are represented as intervals in `clips` where `clips[i]` is an interval starting at time `clips[i][0]` and ending at time `clips[i][1]`, and the costs are given in `costs[i]` for clip `clips[i]`. If the task is impossible, return `-1`. 

Restrictions: `1 <= clips.length <= 100`, `0 <= clips[i][0] <= clips[i][1] <= 100`, `0 <= T <= 100`, `1 <= costs[i] <= 100`.
"""

def minCost(clips, costs, T):
    maxn = 101
    inf = float('inf')
    dp = [0] + [inf]*T
    for i in range(1, T + 1):
        for j in range(len(clips)):
            if clips[j][0] < i and i <= clips[j][1]:
                dp[i] = min(dp[i], dp[clips[j][0]] + costs[j])
    if dp[T] == inf:
        return -1
    return dp[T]