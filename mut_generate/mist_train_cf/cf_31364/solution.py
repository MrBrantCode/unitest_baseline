"""
QUESTION:
Write a function `maxScoreWithoutElimination(scores, threshold)` where scores is a list of integers (2 <= len(scores) <= 10^5, 1 <= scores[i] <= 10^4) representing the scores of the game and threshold is an integer (1 <= threshold <= 10^5) representing the threshold score for elimination. The function should return an integer representing the maximum score a player can achieve without being eliminated.
"""

def maxScoreWithoutElimination(scores, threshold):
    n = len(scores)
    dp = [0] * n
    dp[0] = scores[0]
    dp[1] = scores[1]
    max_score = max(dp[0], dp[1])

    for i in range(2, n):
        dp[i] = max(scores[i], max_score + scores[i])
        max_score = max(max_score, dp[i])

    return max_score if max_score <= threshold else max_score - threshold