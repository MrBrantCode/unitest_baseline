"""
QUESTION:
Given an array of scores representing the scores of a game over consecutive days and an integer k representing the number of consecutive days required to reach a certain milestone, write a function `calculate_total_score(scores, k)` that takes in the array of scores `scores` and the integer `k`, and returns the total score achieved in the minimum number of days required to reach the milestone.

Function signature: `def calculate_total_score(scores: List[int], k: int) -> int`

The function takes in two parameters:
- `scores` (1 <= len(scores) <= 10^5): an array of integers representing the scores on consecutive days.
- `k` (1 <= k <= len(scores)): an integer representing the number of consecutive days required to reach a certain milestone.

The function should return an integer representing the total score achieved in the minimum number of days required to reach the milestone.
"""

from typing import List
import math

def calculate_total_score(scores: List[int], k: int) -> int:
    min_days = math.ceil(len(scores) / k)
    output = 0
    for i in range(min_days):
        output += scores[len(scores) - 1 - i]
    return output