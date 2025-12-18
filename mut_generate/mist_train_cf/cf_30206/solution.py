"""
QUESTION:
Write a function `findOriginalSeries` that takes a list of partial sums of a series as input, where each term is the sum of all previous terms plus the next term in the series, and returns the original series. If multiple valid series exist, return the lexicographically smallest one. The input list will have at least one element, and the output list should have the same number of elements.
"""

from typing import List

def findOriginalSeries(partial_sums: List[float]) -> List[float]:
    n = len(partial_sums)
    original_series = [partial_sums[0]]
    for i in range(1, n):
        original_series.append(partial_sums[i] - partial_sums[i-1])
    return original_series