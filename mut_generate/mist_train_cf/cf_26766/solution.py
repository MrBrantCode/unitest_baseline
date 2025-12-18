"""
QUESTION:
Write a function `calculateTotalScore` that takes a list of integers representing game scores as input and returns the total score. The function should apply a special rule where if the current score is the same as the previous score, the player's total score is doubled; otherwise, the current score is added to the total score. The function should return the total score calculated based on this rule. The input list may contain duplicate scores and scores in any order.
"""

def calculateTotalScore(scores):
    total_score = 0
    prev_score = None
    for score in scores:
        if score == prev_score:
            total_score += score * 2
        else:
            total_score += score
        prev_score = score
    return total_score