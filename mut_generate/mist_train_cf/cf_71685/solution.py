"""
QUESTION:
Create a function called `new_average` that takes a list of original quiz scores and an additional score as input. The function should calculate and return the new average score after adding the additional score to the original scores. The input list of original scores can be of any length, and all scores are positive integers.
"""

def new_average(original_scores, additional_score):
    total_scores = sum(original_scores) + additional_score
    total_quizzes = len(original_scores) + 1
    new_average_score = total_scores / total_quizzes
    return new_average_score