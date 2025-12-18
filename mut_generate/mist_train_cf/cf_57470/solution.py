"""
QUESTION:
Write a function named `maximize_score` that takes a list of positive integers `set`, a list of corresponding point values `scores`, and a positive integer `limit` `L` as input. The function should return the highest attainable point value without exceeding the set limit. The function should ensure that the sum of elements picked from `set` does not exceed `L`, while maximizing the sum of point values that correspond to the picked numbers. The function should not assume any specific values for `set`, `scores`, or `L`.
"""

def maximize_score(set, scores, L):
    dp = [[0 for _ in range(L + 1)] for _ in range(len(set) + 1)]

    for i in range(1, len(set) + 1):
        for j in range(1, L + 1):
            if set[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], scores[i - 1] + dp[i - 1][j - set[i - 1]])
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[-1][-1]