"""
QUESTION:
Write a function `filter_by_prefix_and_suffix` that takes an input list of strings `strings`, a tuple of prefix and suffix `prefix_suffix`, and a minimum length `min_length` as arguments. The function should return a list of strings that start with the given prefix, end with the given suffix, and have a length of at least `min_length`.
"""

from typing import List, Tuple

def filter_by_prefix_and_suffix(strings: List[str], prefix_suffix: Tuple[str, str], min_length: int) -> List[str]:
    return [string for string in strings if string.startswith(prefix_suffix[0]) and string.endswith(prefix_suffix[1]) and len(string) >= min_length]