"""
QUESTION:
Write a function `longest` that takes a list of strings as input and returns the string with the longest length. If multiple strings have the same maximum length, return the first one encountered. If the input list is empty, return None.
"""

from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings: 
        return None

    longest_string = strings[0]
    for string in strings:
        if len(string) > len(longest_string):
            longest_string = string

    return longest_string