"""
QUESTION:
Given a list of integers, write a function `maxNonAdjacentSum` that returns the maximum sum of a contiguous subsequence with no two consecutive elements selected. The input list `arr` contains integers representing participant scores in a coding competition, where 1 <= len(arr) <= 10^5. Each element can be positive, negative, or zero.
"""

from typing import List

def maxNonAdjacentSum(arr: List[int]) -> int:
    if not arr:
        return 0
    incl = 0
    excl = 0
    for i in arr:
        new_excl = max(incl, excl)
        incl = excl + i
        excl = new_excl
    return max(incl, excl)