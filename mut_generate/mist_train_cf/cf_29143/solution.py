"""
QUESTION:
You are given a list of integers representing game scores. Write a function `calculate_total_score(scores)` that takes the list of scores and returns the total score, considering that a score is only valid if the previous two scores are both even, and only valid scores are added to the total. The function should return the total of all valid scores.
"""

from typing import List

def calculate_total_score(scores: List[int]) -> int:
    total_score = 0
    prev_prev_even = False  
    prev_even = False  

    for score in scores:
        if score % 2 == 0:  
            if prev_prev_even and prev_even:  
                total_score += score  
            prev_prev_even, prev_even = prev_even, True  
        else:
            prev_prev_even, prev_even = False, False  

    return total_score