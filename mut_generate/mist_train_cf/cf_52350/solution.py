"""
QUESTION:
Develop a function `count_lists` that takes a list as input and returns a dictionary where each key is a tuple representing a list (including nested lists, which should be flattened first) and the corresponding value is the frequency of the list in the input. The function should ignore non-list items in the input and be efficient for large inputs.
"""

from collections import defaultdict
from typing import Any, List, Tuple

def count_lists(lst: List[Any]) -> dict:
    freq_dict = defaultdict(int)
    for item in lst:
        if isinstance(item, list):
            flat_item = [subitem for sublist in [item] for subitem in (flatten(sublist) if isinstance(sublist, list) else [sublist])]
            freq_dict[tuple(flat_item)] += 1
    return freq_dict

def flatten(lst: List[Any]) -> List[Any]:
    return [item for sublist in lst for item in flatten(sublist)] if isinstance(lst, list) else [lst]