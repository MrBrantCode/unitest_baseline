"""
QUESTION:
Given a list of integers representing participant scores, write a function `min_participants_scored_kth_highest` that takes in the number of participants `n`, the value of `k`, and the list of scores `v`, and returns the minimum number of participants who scored at least the k-th highest score. The function should assume that `n` is equal to the length of `v`, and `1 ≤ k ≤ n`.
"""

from typing import List

def min_participants_scored_kth_highest(n: int, k: int, v: List[int]) -> int:
    v = sorted(v, reverse=True)  # Sort the scores in descending order
    kth_highest_score = v[k-1]  # Get the k-th highest score
    count_kth_highest_or_more = k + v[k:].count(kth_highest_score)  # Count the k-th highest score or more
    return count_kth_highest_or_more