"""
QUESTION:
Write a function `get_unique_sorted_strings` that takes a list of strings as input. The function should return a new list containing only the unique strings from the input list, sorted in ascending order. The function should ignore leading colons (`:`) when comparing strings but preserve the original case of the strings.
"""

from typing import List

def get_unique_sorted_strings(input_list: List[str]) -> List[str]:
    unique_strings = set()
    for string in input_list:
        if string.startswith(':'):
            unique_strings.add(string[1:])  # Remove the leading colon and add to the set
        else:
            unique_strings.add(string)  # Add the string to the set as is
    return sorted(list(unique_strings))  # Convert the set to a list, sort it, and return