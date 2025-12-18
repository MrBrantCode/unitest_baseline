"""
QUESTION:
Create a function `concat_and_remove_duplicates` that takes a list of strings as input, concatenates all the strings, and returns a single string with no duplicate characters. The function should not maintain the original order of characters.
"""

from typing import List

def concat_and_remove_duplicates(str_list: List[str]) -> str:
    concatenated_str = ''.join(str_list)
    unique_chars = set(concatenated_str)
    return ''.join(unique_chars)