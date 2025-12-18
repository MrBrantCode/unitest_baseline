"""
QUESTION:
Create a function `filter_by_prefix_and_suffix` that takes a list of strings and a tuple containing a prefix and a suffix. The function should return a new list containing only the strings from the input list that start with the given prefix and end with the given suffix.
"""

from typing import List, Tuple

def filter_by_prefix_and_suffix(strings: List[str], prefix_suffix: Tuple[str, str]) -> List[str]:
    prefix, suffix = prefix_suffix
    return [s for s in strings if s.startswith(prefix) and s.endswith(suffix)]