"""
QUESTION:
Write a function `find_pivot_value` that takes a list of integers `list_data` and an integer `pivot_index` as input, and returns the value at the `pivot_index` in `list_data` if it is within the list's range. If `pivot_index` is out of range, the function should return "Index out of range".
"""

from typing import List, Union

def find_pivot_value(list_data: List[int], pivot_index: int) -> Union[int, str]:
    if pivot_index < 0 or pivot_index >= len(list_data):
        return "Index out of range"
    else:
        return list_data[pivot_index]