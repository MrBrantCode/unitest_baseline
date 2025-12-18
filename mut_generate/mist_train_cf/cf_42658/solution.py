"""
QUESTION:
Write a function `maxNonAdjacentSum` that takes a list of integers representing scores as input and returns the maximum possible sum of non-adjacent scores. No two chosen scores can be adjacent in the original list. The function should return an integer value representing the maximum sum.

Restrictions: The input list can be empty or contain one or more integers.
"""

from typing import List

def maxNonAdjacentSum(scores: List[int]) -> int:
    if not scores:
        return 0
    if len(scores) <= 2:
        return max(scores)
    
    max_sum = [0] * len(scores)
    max_sum[0] = scores[0]
    max_sum[1] = max(scores[0], scores[1])
    
    for i in range(2, len(scores)):
        max_sum[i] = max(max_sum[i-1], max_sum[i-2] + scores[i])
    
    return max_sum[-1]