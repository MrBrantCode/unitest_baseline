"""
QUESTION:
Function `minDistance` takes two parameters: a list of unique integers `houses` and an integer `k`. The task is to assign `k` mailboxes along the street, where each mailbox can only be situated at a dwelling's location. The goal is to find the minimum cumulative distance between each dwelling and its nearest mailbox. If there are multiple solutions with the same minimum cumulative distance, choose the one with the smallest maximum distance from a dwelling to a mailbox. 

Restrictions:
- `1 <= len(houses) <= 100`
- `1 <= houses[i] <= 10^4`
- `1 <= k <= len(houses)`
- The array `houses` contains unique integers.
"""

def minDistance(houses, k):
    n = len(houses)
    houses.sort()
    cost = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            median = houses[(i+j)//2]
            cost[i][j] = sum(abs(houses[x] - median) for x in range(i, j+1))
    dp = [[float('inf')] * (k+1) for _ in range(n)]
    dp[0][1] = 0
    for i in range(n):
        for j in range(1, min(i+2, k+1)):
            for m in range(i):
                dp[i][j] = min(dp[i][j], dp[m][j-1] + cost[m+1][i])
    return dp[n-1][k]