"""
QUESTION:
Given a list of integers representing game scores, write a function `calculateFinalScore(scores)` that calculates the final score of the game. The final score is the sum of the scores of the last two turns, but if the last two turns have the same score, the score is doubled. The input list `scores` contains integers between 0 and 100 inclusive. The function should return the final score as an integer.
"""

def calculateFinalScore(scores):
    if len(scores) < 2:
        return sum(scores)
    last_score = scores[-1]
    second_last_score = scores[-2]
    if last_score == second_last_score:
        return sum(scores[:-2]) + last_score * 2
    else:
        return sum(scores)