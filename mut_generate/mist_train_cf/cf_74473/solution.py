"""
QUESTION:
Create a function `average_score` that takes an array of tuples as input, where each tuple contains a unique identifier followed by three scores. The function should calculate the mean score for each individual and return a dictionary where the keys are the unique identifiers and the values are the corresponding mean scores. The mean scores should be rounded to two decimal places.
"""

def average_score(arr):
    result = {}
    for tup in arr:
        id_ = tup[0]
        avg_score = round(sum(tup[1:]) / len(tup[1:]), 2)
        result[id_] = avg_score
    return result