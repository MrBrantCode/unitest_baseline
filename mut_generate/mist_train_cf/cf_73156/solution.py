"""
QUESTION:
Write a function called `rolling_max` that takes a list of integers as input and returns a new list where each element at each index is the maximum value from the input list up to that index. Assume the input list contains at least one element.
"""

from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ From the provided sequence of integers, manufacture a list of the progressively highest value at each point in the series.
    """
    max_num = numbers[0]
    result = [max_num]

    for i in numbers[1:]:
        if i > max_num:
            max_num = i
        result.append(max_num)

    return result