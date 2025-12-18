"""
QUESTION:
Create a function `find_substring_indices` that returns all non-overlapping occurrences of a given substring in a string as a list of tuples, where each tuple contains the starting and ending indices of an occurrence. The function should be case-sensitive and have a time complexity of O(n), where n is the length of the input string. The function should take two parameters: `string` and `substring`, both of type `str`, and return a list of tuples of integers.
"""

from typing import List, Tuple

def find_substring_indices(string: str, substring: str) -> List[Tuple[int, int]]:
    indices = []
    sub_len = len(substring)
    for i in range(len(string)):
        if string[i:i+sub_len] == substring:
            indices.append((i, i+sub_len-1))
    return indices