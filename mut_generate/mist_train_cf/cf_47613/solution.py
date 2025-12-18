"""
QUESTION:
Implement a function named `remove_duplicates` that takes a sorted list of integers `numbers` and an integer `threshold` as input. The function should use binary search to remove recurring elements that appear more than the specified `threshold` times while maintaining the order of the remaining items. The solution must adhere to the O(log n) time complexity requirement.
"""

from typing import List
from bisect import bisect_left, bisect_right

def remove_duplicates(numbers: List[int], threshold: int) -> List[int]: 
    final_numbers = []
    i = 0
    n = len(numbers)

    while i<n:
        low = bisect_left(numbers, numbers[i])
        high = bisect_right(numbers, numbers[i])
        if high - low <= threshold and numbers[i] not in final_numbers:
            final_numbers.append(numbers[i])
        i = high
    return final_numbers