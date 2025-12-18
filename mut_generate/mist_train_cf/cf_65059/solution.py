"""
QUESTION:
Given an array `houses` and an integer `k`, where `houses[i]` is the location of the ith house along a street, write a function `minDistance(houses, k)` to allocate `k` mailboxes in the street such that the mailboxes must be placed at the location of a house. The function should return the minimum total distance between each house and its nearest mailbox. If it is not possible to place `k` mailboxes at the location of a house, return -1.

Constraints:
- `n == houses.length`
- `1 <= n <= 100`
- `1 <= houses[i] <= 10^4`
- `1 <= k <= n`
- Array `houses` contains unique integers.
"""

def minDistance(houses, k):
    houses = sorted(houses)
    n = len(houses)

    cost = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            mid = (i + j) // 2
            cost[i][j] = sum(abs(houses[mid] - houses[x]) for x in range(i, j+1))

    dp = [[float('inf')]*k for _ in range(n)]
    dp[0][0] = 0
    for i in range(1, n):
        dp[i][0] = cost[0][i]
        for j in range(1, min(i+1, k)):
            for p in range(i):
                dp[i][j] = min(dp[i][j], dp[p][j-1] + cost[p+1][i])

    return dp[-1][-1]