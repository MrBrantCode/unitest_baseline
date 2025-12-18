"""
QUESTION:
Write a function `calculate_statistics` that takes an array of integers `scores` as input and returns the maximum score, minimum score, average score, and median score without using any built-in sorting functions or libraries. The function should implement its own sorting algorithm with a time complexity of O(n^2) to find the median score.
"""

def calculate_statistics(scores):
    # Find max and min scores
    max_score = scores[0]
    min_score = scores[0]
    sum_scores = 0
    for score in scores[1:]:
        if score > max_score:
            max_score = score
        if score < min_score:
            min_score = score
        sum_scores += score

    # Calculate average score
    average_score = (sum_scores + scores[0]) / len(scores)

    # Sort the array using bubble sort
    for i in range(len(scores)-1):
        for j in range(len(scores)-1-i):
            if scores[j] > scores[j+1]:
                scores[j], scores[j+1] = scores[j+1], scores[j]

    # Find median score
    if len(scores) % 2 == 0:
        median_score = (scores[len(scores)//2-1] + scores[len(scores)//2]) / 2
    else:
        median_score = scores[len(scores)//2]

    return max_score, min_score, average_score, median_score