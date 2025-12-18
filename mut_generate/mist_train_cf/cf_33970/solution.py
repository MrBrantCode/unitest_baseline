"""
QUESTION:
Write a function `calculateFinalScore(scores)` that takes in a list of integers `scores` with a length between 1 and 100. The function should calculate the final score of a game where each turn's score is the sum of the last two turns' scores, unless the last two turns have the same score, in which case the score is doubled. Return the total score of the game.
"""

def calculateFinalScore(scores):
    total_score = 0
    prev_score = 0
    prev_prev_score = 0
    for score in scores:
        if score == prev_score and score == prev_prev_score:
            total_score += score * 2
        else:
            total_score += score
        prev_prev_score = prev_score
        prev_score = score
    return total_score