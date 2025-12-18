"""
QUESTION:
Create a function named `find_min_max` that takes a list of integers and an optional boolean keyword argument `return_sorted` (defaulting to `False`). The function should return a tuple containing the smallest and largest integers in the list. If `return_sorted` is `True`, the tuple should also include a sorted copy of the list from smallest to largest.
"""

from typing import List, Union, Tuple

def find_min_max(numbers: List[int], return_sorted: bool = False) -> Union[Tuple[int, int], Tuple[int, int, List[int]]]:
    min_num = min(numbers)
    max_num = max(numbers)
    
    if return_sorted:
        return min_num, max_num, sorted(numbers)
    else:
        return min_num, max_num