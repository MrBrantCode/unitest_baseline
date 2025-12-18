"""
QUESTION:
Write a Python function `calculate_option_scores` that takes in three dictionaries: `scores`, `weights`, and `answers`. The `scores` dictionary maps each option (A, B, C, D) to a list of four scores (1, 2, 3, 4) in a specific order. The `weights` dictionary maps each question (Q1 through Q10) to a weight between 1 and 10. The `answers` dictionary maps each question to a list of four options (A, B, C, D). The function should calculate the score for each option by multiplying the score of each answer by the weight of the question and summing the results. The function should then return the scores for each option in decreasing order.
"""

def calculate_option_scores(scores, weights, answers):
    option_scores = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
    for question in answers:
        weight = weights[question]
        for i, option in enumerate(answers[question]):
            option_scores[option] += weight * scores[option][i]
    return sorted(option_scores.items(), key=lambda x: x[1], reverse=True)