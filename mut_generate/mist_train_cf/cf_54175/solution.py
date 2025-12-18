"""
QUESTION:
Write a function `maxVacationDays` that takes four parameters: `flights`, `days`, `costs`, and `B`. The function should return the maximum number of vacation days that can be taken given the provided constraints.

The `flights` matrix represents the airline status from city `i` to city `j`, where `flights[i][j] = 0` if there's no flight and `flights[i][j] = 1` if there is a flight. The `days` matrix represents the maximum vacation days that can be taken in city `i` in week `j`. The `costs` matrix represents the cost of flights from city `i` to city `j`, and `B` is the total budget for flights. The journey begins in city `0` on a Monday, and the employee has `K` weeks to travel.
"""

def maxVacationDays(flights, days, costs, B):
    K = len(days[0])
    N = len(flights)
    dp = [[-1] * (B + 1) for _ in range(K)]

    for d in range(B + 1):
        if d == 0:
            dp[0][d] = days[0][0]
        else:
            for u in range(N):
                for v in range(N):
                    if flights[u][v] == 0 or u == v:
                        continue
                    if costs[u][v] > d:
                        continue
                    for last_d in range(d - costs[u][v] + 1):
                        dp[0][d] = max(dp[0][d], dp[0][last_d] + days[v][0] if dp[0][last_d] != -1 else -1)

    for k in range(1, K):
        for d in range(B + 1):
            for u in range(N):
                for v in range(N):
                    if flights[u][v] == 0 or u == v:
                        continue
                    if costs[u][v] > d:
                        continue
                    for last_d in range(d - costs[u][v] + 1):
                        dp[k][d] = max(dp[k][d], dp[k - 1][last_d] + days[v][k] if dp[k - 1][last_d] != -1 else -1)

    ans = -1
    for d in range(B + 1):
        ans = max(ans, dp[K - 1][d])
    return ans