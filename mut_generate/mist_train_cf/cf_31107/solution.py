"""
QUESTION:
Implement the `filter_names` function that filters out names from a given list of strings. The function should exclude names that match the following criteria:
- Names that are exactly 'In', 'Out', 'get_ipython', 'exit', or 'quit'.
- Names that start with an underscore ('_').
Return a new list containing only the names that do not meet these filtering criteria.

Function Signature: `def filter_names(names: List[str]) -> List[str]`
"""

from typing import List

def filter_names(names: List[str]) -> List[str]:
    filtered_names = [name for name in names if name not in ['In', 'Out', 'get_ipython', 'exit', 'quit'] and not name.startswith('_')]
    return filtered_names