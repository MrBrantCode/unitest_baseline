"""
QUESTION:
Create a function named `advanced_filter` that takes in a list of strings and a tuple of three strings representing a prefix, a suffix, and an infix. The function should return a list of strings from the input list that start with the prefix, end with the suffix, and contain the infix. The function must be implemented using recursion.
"""

from typing import List, Tuple

def advanced_filter(strings: List[str], prefix_suffix_inner: Tuple[str, str, str]) -> List[str]:
    # base case: if the strings list is empty, return an empty list
    if not strings:
        return []

    prefix, suffix, infix = prefix_suffix_inner

    head, *tail = strings

    # check if the string meets the conditions
    if head.startswith(prefix) and head.endswith(suffix) and infix in head:
        # if it does, add it to the result and continue with the rest of the list
        return [head] + advanced_filter(tail, prefix_suffix_inner)
    else:
        # if it doesn't, skip it and continue with the rest of the list
        return advanced_filter(tail, prefix_suffix_inner)