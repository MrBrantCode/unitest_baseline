"""
QUESTION:
Write a function `mincostTickets(days, costs, maxPasses)` that takes as input a list of days `days` representing the days of the year that you will travel, a list of costs `costs` representing the costs of 1-day, 7-day, 30-day, and 365-day passes, and an integer `maxPasses` representing the maximum number of passes that can be bought in a year.

The function should return the minimum number of dollars you need to travel every day in the given list of `days` under the constraint that you can only buy a maximum of `maxPasses` number of passes in a year.

Constraints: `1 <= days.length <= 365`, `1 <= days[i] <= 365`, `days` is in strictly increasing order, `costs.length == 4`, `1 <= costs[i] <= 1000`, and `1 <= maxPasses <= 10`.
"""

def mincostTickets(days, costs, maxPasses):
    dp = [[0]*11 for _ in range(366)]
    dayset = set(days)
    for i in range(1, 366):
        for j in range(1, 11):
            if i not in dayset:
                dp[i][j] = dp[i-1][j]
            else:
                c1 = costs[0] + dp[i-1][j-1] if i-1>=0 and j>=1 else float('inf')
                c7 = costs[1] + dp[i-7][j-1] if i-7>=0 and j>=1 else float('inf')
                c30 = costs[2] + dp[i-30][j-1] if i-30>=0 and j>=1 else float('inf')
                c365 = costs[3] + dp[i-365][j-1] if i-365>=0 and j>=1 else float('inf')
                dp[i][j] = min(c1, c7, c30, c365)
    return dp[365][maxPasses]