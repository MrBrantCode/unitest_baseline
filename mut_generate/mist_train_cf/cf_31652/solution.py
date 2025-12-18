"""
QUESTION:
Write a function named `get_allowed_numbers` that takes a list of ranges as input, where each range is a tuple of two integers representing the start and end of the range (inclusive), and returns a list of all numbers within the given ranges, sorted in ascending order, with no duplicates. If a range contains only one number, it should be included in the output. Empty ranges should be ignored.
"""

from typing import List, Tuple

def entrance(ranges: List[Tuple[int, int]]) -> List[int]:
    allowed_list = set()
    for range_start, range_end in ranges:
        if range_start <= range_end:
            allowed_list.update(range(range_start, range_end + 1))
    return sorted(list(allowed_list))