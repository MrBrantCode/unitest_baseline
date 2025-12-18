"""
QUESTION:
Write a function `rolling_avg_median` that takes a list of integers as input and returns a list of tuples, where each tuple contains the running average and median of the input list up to that point. The function should exclude any duplicate tuples from the output.
"""

import bisect
from typing import List, Tuple

def rolling_avg_median(numbers: List[int]) -> List[Tuple[float, float]]:
    total = 0
    sorted_numbers = []
    result = []

    for i, num in enumerate(numbers):
        total += num
        bisect.insort(sorted_numbers, num)
        avg = total / (i + 1)
        if i % 2 == 0:
            median = sorted_numbers[i // 2]
        else:
            median = (sorted_numbers[(i // 2)] + sorted_numbers[(i // 2) + 1]) / 2.0
        result.append((avg, median))

    result = [(round(avg, 2), round(median, 2)) for avg, median in result if result.count((avg, median)) == 1]
    return result