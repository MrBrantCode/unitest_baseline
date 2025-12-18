"""
QUESTION:
Implement a function `longest_term(terms, limit)` where `terms` is a list of tuples, each tuple representing a linguistic term with its length and penalty points. The function should return the maximum length of a term that can be constructed without exceeding the given `limit` on penalty points.
"""

def longest_term(terms, limit):
    dp = [[0 for _ in range(limit + 1)] for __ in range(len(terms) + 1)]
    for i in range(1, len(terms) + 1):
        for j in range(limit + 1):
            if terms[i - 1][1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - terms[i - 1][1]] + terms[i - 1][0])
    return dp[-1][-1]