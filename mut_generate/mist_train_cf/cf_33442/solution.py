"""
QUESTION:
Write a function `maxPossibleScore(scores)` that takes in a list of integers `scores` (1 <= len(scores) <= 10^5) and returns the maximum possible score that can be achieved by selecting a subset of players in a circular arrangement where each player's score is the sum of the scores of the two adjacent players.
"""

def maxPossibleScore(scores):
    n = len(scores)
    if n == 1:
        return scores[0]
    elif n == 2:
        return max(scores)

    # Initialize an array to store the maximum possible scores for each player
    max_scores = [0] * n

    # Calculate the maximum possible score for the first two players
    max_scores[0] = scores[0]
    max_scores[1] = max(scores[0], scores[1])

    # Calculate the maximum possible score for the remaining players
    for i in range(2, n):
        max_scores[i] = max(max_scores[i-1], max_scores[i-2] + scores[i])

    # Return the maximum possible score for the last player
    return max_scores[-1]