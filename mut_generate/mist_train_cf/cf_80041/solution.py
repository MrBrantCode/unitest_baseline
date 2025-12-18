"""
QUESTION:
You are given three N*N matrices: flights, costs, and an N*K matrix days, along with a budget B. You need to write a function `maxVacationDays(flights, days, costs, B)` to find the maximum vacation days you could take during K weeks. The function should return the maximum possible vacation days. 

The function should consider the rules and restrictions: 
- flights[i][j] = 1 if there is a flight from city i to city j, otherwise flights[i][j] = 0.
- days[i][j] represents the maximum days you could take vacation in the city i in the week j.
- costs[i][j] represents the cost of the flight from city i to city j.
- The total budget for flights is B dollars.
- N and K are positive integers in the range [1, 100].
- The values in the flights matrix are integers in the range [0, 1].
- The values in the days matrix are integers in the range [0, 7].
- The values in the costs matrix are integers in the range [0, 1000].
"""

def maxVacationDays(flights, days, costs, B):
    N, K = len(days), len(days[0])
    dp = [[-float('inf')] * N for _ in range(K+1)]
    dp[0][0] = 0
    budget = [B] * N
    for i in range(1, K+1):
        for j in range(N):
            for k in range(N):
                if (j == k or flights[k][j]) and budget[k] >= costs[k][j]:
                    dp[i][j] = max(dp[i][j], dp[i-1][k] + days[j][i-1])
            if j != 0:
                budget[j] -= costs[j][0]
    return max(dp[-1])