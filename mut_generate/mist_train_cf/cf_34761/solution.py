"""
QUESTION:
Write a function `sort_results` that takes a list of tuples `results` as input and returns a new list containing the sorted results based on the third element of each tuple in descending order. Each tuple in the `results` list contains three elements. The `sort_results` function should not modify the original list.
"""

from typing import List, Tuple, Any

def sort_results(results: List[Tuple[Any, Any, Any]]) -> List[Tuple[Any, Any, Any]]:
    return sorted(results, key=lambda r: -r[2])