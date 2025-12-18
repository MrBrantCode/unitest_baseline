"""
QUESTION:
Write a function `calculate_average_score(scores)` that takes a list of integers `scores` with a length between 2 and 100, and returns the average score rounded to two decimal places after excluding the highest and lowest scores. The function should handle both positive and negative integers and return `0.00` if the list of scores is empty after removing the highest and lowest scores.
"""

def calculate_average_score(scores):
    if len(scores) <= 2:
        return 0.00  

    scores.sort()  
    scores = scores[1:-1]  

    if scores:  
        average = sum(scores) / len(scores)  
        return round(average, 2)  
    else:
        return 0.00  