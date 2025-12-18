"""
QUESTION:
Given a list of integers representing game scores, write a function `calculate_total_score(scores)` that calculates the total score for the game. The total score is the sum of the scores of the last two turns, but if the last two scores are the same, the player's score is doubled. The scores list contains integers from 0 to 100. The function should return an integer representing the total score for the game.
"""

def entrance(scores):
    total_score = 0
    n = len(scores)
    for i in range(2, n):
        if scores[i-1] == scores[i-2]:
            total_score += 2 * scores[i]
        else:
            total_score += scores[i]
    return total_score