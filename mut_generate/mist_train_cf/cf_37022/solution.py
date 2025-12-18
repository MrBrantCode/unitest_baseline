"""
QUESTION:
Write a function `find_common_set_of_column_names` that takes a list of tuples of integers as input and returns a set of integers representing the common column names (0-indexed) that are present in all tuples. The input list has a length between 1 and 100, and all tuples have the same length. The function should return an empty set if the input list is empty.
"""

from typing import List, Tuple, Set

def find_common_set_of_column_names(vals: List[Tuple[int, ...]]) -> Set[int]:
    if not vals:
        return set()

    common_columns = set(range(len(vals[0])))  

    for tuple_vals in vals[1:]:
        common_columns = common_columns.intersection(set(i for i, _ in enumerate(tuple_vals)))

    return common_columns