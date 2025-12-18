"""
QUESTION:
Write a function `range_counter` that takes a list of integers `values`, an integer `range_start`, and an integer `range_end` as input. The function should return a tuple containing the number of 'hits' (values within the range) and 'out of range' (values outside the range) in the list. The range is inclusive of both `range_start` and `range_end`.
"""

from typing import List, Tuple

def range_counter(values: List[int], range_start: int, range_end: int) -> Tuple[int, int]:
    hit = 0
    out_of_range = 0

    for value in values:
        if value >= range_start and value <= range_end:
            hit += 1
        else:
            out_of_range += 1
            
    return (hit, out_of_range)