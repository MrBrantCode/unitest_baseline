"""
QUESTION:
Given a list of integers representing game scores, write a function `calculate_total_score(scores)` that calculates the total score according to the game's rule. The rule states that a player's score is the sum of the scores of the last two turns, but if the last two scores are the same, the player's score is doubled. The list `scores` contains integers in the range 0 to 100. The function should return an integer representing the total score.
"""

def calculate_total_score(scores):
    total_score = 0
    prev_score = 0
    prev_prev_score = 0
    for score in scores:
        if prev_prev_score == prev_score == score:
            total_score += 2 * score
        else:
            total_score += score
        prev_prev_score = prev_score
        prev_score = score
    return total_score