"""
QUESTION:
Write a function `average_score` that calculates the weighted average score for each person given a list of tuples containing a person's name and their scores in three subjects, and a list of weights for the three subjects. The function should return a dictionary where the key is the person's name and the value is their weighted average score. Ensure that the weights sum up to 1 and each person has three subject scores.
"""

def average_score(scores, weights):
    if len(weights) != 3:
        raise Exception("The weights should be provided for three subjects.")
    if not all(isinstance(weight, (int, float)) for weight in weights):
        raise Exception("Weights should be numbers.")
    if abs(sum(weights) - 1) > 1e-6:
        raise Exception("Weights should sum up to 1.")
    averages = {}
    for person, subject_scores in scores:
        if len(subject_scores) != 3:
            raise Exception("Each person should have three subject scores.")
        if not all(isinstance(score, (int, float)) for score in subject_scores):
            raise Exception("All subject scores should be numbers.")
        averages[person] = sum(subject_score * weight for subject_score, weight in zip(subject_scores, weights))
    return averages