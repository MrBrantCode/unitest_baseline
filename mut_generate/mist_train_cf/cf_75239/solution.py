"""
QUESTION:
Function name: maxScore(cardPoints, k)

Description: Given an integer array `cardPoints` and an integer `k`, return the maximum score that can be obtained by taking exactly `k` cards from the beginning or end of the row, where the next card from the beginning or end will have its points doubled if a card is taken from that end.

Restrictions: `1 <= cardPoints.length <= 10^5`, `1 <= cardPoints[i] <= 10^4`, and `1 <= k <= cardPoints.length`.
"""

def maxScore(cardPoints, k):
    n = len(cardPoints)
    dp = [0] * (k+1)

    # Initialize dp array with first element
    dp[0] = ((2**0) * cardPoints[n - 1])

    # Initialize first column
    for i in range(1, k+1):
        dp[i] = dp[i-1] + ((2**i) * cardPoints[n - i])

    # DP calculation
    res = dp[k]
    for i in range(1, k+1):
        dp[i] = max(dp[i], ((2**i) * cardPoints[i - 1]) + dp[i - 1])
        res = max(res, dp[i] + (dp[k-i] - (2**i * cardPoints[i-1])))
    return res