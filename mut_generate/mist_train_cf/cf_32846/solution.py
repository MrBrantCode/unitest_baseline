"""
QUESTION:
Implement a function named `get_unique_strings` that takes a list of strings as input and returns a new list containing only unique strings from the input list. The function should exclude duplicate strings and preserve the original order of the strings in the input list. The function signature should be `def get_unique_strings(input_list: List[str]) -> List[str]:`.
"""

from typing import List

def get_unique_strings(input_list: List[str]) -> List[str]:
    unique_strings = []
    for string in input_list:
        if string not in unique_strings:
            unique_strings.append(string)
    return unique_strings