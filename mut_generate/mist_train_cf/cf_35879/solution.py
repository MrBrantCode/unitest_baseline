"""
QUESTION:
Calculate the scores of players in a game with a special scoring rule. The score of each player is the sum of their own score and the scores of the players immediately before and after them. If a player has no adjacent players, their score is their own score.

The function `calculate_scores(scores)` takes a list of integers `scores` as input and returns a new list where each element represents the score of the corresponding player according to the special rule.

Restrictions:
- The input list `scores` contains integers between -1000 and 1000 and has a length between 1 and 10^5.
- Return a list of integers where each element represents the score of the corresponding player according to the special rule.
"""

from typing import List

def entrance(scores: List[int]) -> List[int]:
    n = len(scores)
    if n == 1:
        return scores

    result = [0] * n
    result[0] = scores[0] + scores[1]
    result[n - 1] = scores[n - 1] + scores[n - 2]

    for i in range(1, n - 1):
        result[i] = scores[i - 1] + scores[i] + scores[i + 1]

    return result