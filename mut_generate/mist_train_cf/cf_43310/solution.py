"""
QUESTION:
Write a function `nested_list_sum(lst)` that takes in a nested list of numbers as input, where each element can be either a floating-point number or another nested list. The function should return the sum of all the floating-point numbers in the list.
"""

from typing import List, Union

def nested_list_sum(lst: List[Union[float, List]]) -> float:
    total_sum = 0.0
    for item in lst:
        if isinstance(item, float):
            total_sum += item
        elif isinstance(item, list):
            total_sum += nested_list_sum(item)
    return total_sum