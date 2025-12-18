"""
QUESTION:
Create a function called `filter_and_sort_strings` that takes a list of strings, a tuple of prefix and suffix, and an integer as input. The function should filter the list of strings to include only those that start with the given prefix, end with the given suffix, and have a length of at least the given integer. The function should then sort the filtered list of strings in lexicographic order and return it.
"""

from typing import List, Tuple

def filter_and_sort_strings(strings: List[str], prefix_suffix: Tuple[str, str], n: int) -> List[str]:
    filtered = [s for s in strings if s.startswith(prefix_suffix[0]) and s.endswith(prefix_suffix[1]) and len(s) >= n]
    return sorted(filtered)