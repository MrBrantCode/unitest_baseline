"""
QUESTION:
Write a function `calculate_score_frequency(b)` that takes a pandas DataFrame `b` with a 'score' column as input, and returns a dictionary where the keys are the unique scores in the 'score' column and the values are the frequencies of each score in the dataset. The function should return the frequency of each unique score, with no specific ordering or sorting required.
"""

def calculate_score_frequency(b):
    score_counts = b['score'].value_counts().to_dict()
    return score_counts