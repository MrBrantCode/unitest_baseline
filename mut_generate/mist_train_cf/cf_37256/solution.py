"""
QUESTION:
Write a function `calculateTotalScore(scores)` where `scores` is a list of integers representing the scores of a game, with the length of the list being at least 2 and at most 1000. The function should return an integer representing the total score of the game, calculated by summing the first two scores and then adding the sum of the previous two scores for each subsequent round.
"""

def entance(scores):
    if len(scores) < 2:
        return 0
    elif len(scores) == 2:
        return sum(scores)
    else:
        total_score = sum(scores[:2])
        prev_prev_score = scores[0]
        prev_score = scores[1]
        for i in range(2, len(scores)):
            current_score = prev_prev_score + prev_score
            total_score += current_score
            prev_prev_score = prev_score
            prev_score = current_score
        return total_score