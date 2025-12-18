"""
QUESTION:
Create a function named `rolling_max_min` that takes a list of integers as input and returns a list of tuples, where each tuple contains the maximum and minimum values up to that point in the sequence, excluding negative integers and duplicate pairs.
"""

from typing import List, Tuple

def rolling_max_min(numbers: List[int]) -> List[Tuple[int, int]]:
    if len(numbers) == 0:
        return []
    numbers = list(filter(lambda x: x >= 0, numbers))
    if len(numbers) == 0:
        return []
    min_val = numbers[0]
    max_val = numbers[0]
    old_max, old_min = max_val, min_val
    ans = [(max_val, min_val)]
    for i in range(1, len(numbers)):
        if numbers[i] < min_val:
            min_val = numbers[i]
        if numbers[i] > max_val:
            max_val = numbers[i]
        if old_min != min_val or old_max != max_val:
            ans.append((max_val, min_val))
            old_max, old_min = max_val, min_val
    return ans