"""
QUESTION:
Write a function `calculate_scores(scoring_events)` that takes a list of tuples, where each tuple contains a score and the number of ways to achieve that score, and returns a list of integers representing the total number of ways to achieve each score after each scoring event in chronological order. The function should assume that the input list is not empty and that the scoring events are given in chronological order. The function should also handle cases where the score is zero or negative. 

Function signature: `def calculate_scores(scoring_events: List[Tuple[int, int]]) -> List[int]`
"""

from typing import List, Tuple

def calculate_scores(scoring_events: List[Tuple[int, int]]) -> List[int]:
    dictionary_of_scores = {}
    list_to_return = []
    for score, number_of_ways in scoring_events:
        new_score = score
        if new_score != 0:
            dictionary_of_scores[new_score] = dictionary_of_scores.get(new_score, 0) + number_of_ways
        list_to_return.append(sum(dictionary_of_scores.values()))
    return list_to_return