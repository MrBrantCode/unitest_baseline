"""
QUESTION:
Create a function called `filter_and_sort_strings` that filters a list of strings based on their length and returns a new list with the filtered strings. The function should take two parameters: `string_list` (a list of strings) and `min_length` (a positive integer representing the minimum length threshold). The function should return a new list containing only the strings from the input list that have a length greater than or equal to the minimum length threshold. The strings in the new list should be sorted in descending order based on their length. If two strings have the same length, they should be sorted in alphabetical order.
"""

from typing import List

def filter_and_sort_strings(string_list: List[str], min_length: int) -> List[str]:
    filtered_strings = [string for string in string_list if len(string) >= min_length]
    filtered_strings.sort(key=lambda x: (-len(x), x))
    return filtered_strings