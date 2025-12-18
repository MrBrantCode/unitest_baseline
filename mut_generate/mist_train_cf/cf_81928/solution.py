"""
QUESTION:
Write a function named `rolling_avg_median` that takes a list of integers as input and returns a list of tuples, where each tuple contains the mean and median of the input list up to that point. The function should not include any duplicate mean and median pairs in its output.
"""

from typing import List, Tuple
import numpy as np

def rolling_avg_median(numbers: List[int]) -> List[Tuple[float, float]]:
    means_medians = set()
    ans = []
    for i in range(len(numbers)):
        sequence = numbers[:i+1]
        mean = np.mean(sequence)
        median = np.median(sequence)
        tuple_mean_median = (mean, median)
        if tuple_mean_median not in means_medians:
            ans.append(tuple_mean_median)
            means_medians.add(tuple_mean_median)
    return ans