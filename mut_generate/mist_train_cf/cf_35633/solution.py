"""
QUESTION:
Implement a function `sort_by_second_element` that takes a list of tuples as input and returns a new list of tuples sorted based on the second element of each tuple in ascending order. The input list can contain tuples with elements of any data type. The function should not modify the original list.
"""

from typing import List, Tuple, Any

def entrance(lst: List[Tuple[Any, Any]]) -> List[Tuple[Any, Any]]:
    return sorted(lst, key=lambda x: x[1])