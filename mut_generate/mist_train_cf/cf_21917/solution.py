"""
QUESTION:
Create a function named `filter_and_sort_strings` that takes two parameters: `string_list` and `min_length`. The function should filter the strings in `string_list` based on their length, returning a new list containing only the strings with a length greater than or equal to `min_length`. The returned list should be sorted in descending order by string length, with ties broken by alphabetical order. The function should handle edge cases, such as an empty input list or a minimum length threshold of zero.
"""

from typing import List

def filter_and_sort_strings(string_list: List[str], min_length: int) -> List[str]:
    filtered_list = [s for s in string_list if len(s) >= min_length]
    sorted_list = sorted(filtered_list, key=lambda s: (-len(s), s))
    return sorted_list