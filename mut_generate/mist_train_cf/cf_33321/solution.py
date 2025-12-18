"""
QUESTION:
Write a function `calculate_average_score` that takes a list of integers `scores` with a length of at least 4 and returns the average score, rounded to the nearest integer, after excluding the highest and lowest scores.
"""

def calculate_average_score(scores):
    if len(scores) < 4:
        return 0  

    scores.sort()  
    trimmed_scores = scores[1:-1]  
    average_score = round(sum(trimmed_scores) / len(trimmed_scores))  
    return average_score