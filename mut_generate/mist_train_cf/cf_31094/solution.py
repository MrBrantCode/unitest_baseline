"""
QUESTION:
Implement a function `sum_max_min_tuple` that takes a list of integers as input and returns a tuple containing three elements: the sum of all the integers, the maximum value, and the minimum value. The input list may be empty, in which case the function should return a tuple of three zeros.
"""

from typing import List, Tuple

def sum_max_min_tuple(input_list: List[int]) -> Tuple[int, int, int]:
    if not input_list:
        return (0, 0, 0)  

    sum_of_integers = sum(input_list)
    max_value = max(input_list)
    min_value = min(input_list)

    return (sum_of_integers, max_value, min_value)