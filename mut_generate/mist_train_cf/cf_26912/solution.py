"""
QUESTION:
Write a function `calculateTotalScore` that takes a list of integers representing game scores, and two integers representing fixed scores for the first two rounds. The function should return the total score of the game where each player's score is the sum of their scores from the previous two rounds, except for the first two rounds which have fixed scores. The list of scores has a length between 1 and 10^5, and the fixed scores for the first two rounds are between 0 and 100.
"""

def calculateTotalScore(scores, round1, round2):
    total_score = round1 + round2
    prev_score = round2
    prev_prev_score = round1
    for score in scores:
        total_score += score
        new_score = prev_score + score
        prev_prev_score = prev_score
        prev_score = new_score
    return total_score