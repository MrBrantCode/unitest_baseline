"""
QUESTION:
Write a function `calculate_average_score` that takes a list of integers `scores` as input and returns the average score calculated as the sum of all scores divided by the count of distinct scores. The function should handle both positive and negative integers and return a floating-point number.
"""

def calculate_average_score(scores):
    distinct_scores = set(scores)  
    sum_of_scores = sum(scores)  
    average_score = sum_of_scores / len(distinct_scores)  
    return average_score