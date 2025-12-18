"""
QUESTION:
Write a function called `top_two` that takes a list of strings as input and returns a tuple containing the longest and second longest strings. If there is only one string in the list, return the string and `None`. If the list is empty, return `(None, None)`. If multiple strings have the same length, return the first string of each length.
"""

from typing import List, Optional, Tuple

def top_two(strings: List[str]) -> Optional[Tuple[str, str]]:
    sorted_strings = sorted(strings, key=len, reverse=True)
    longest = sorted_strings[0] if sorted_strings else None
    second_longest = sorted_strings[1] if len(sorted_strings) > 1 else None
    return longest, second_longest