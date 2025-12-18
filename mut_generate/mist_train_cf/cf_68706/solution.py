"""
QUESTION:
Write a function `longest` that takes a list of strings and an integer `k` as input, and returns the `k` longest strings in the order of their occurrence. If the list is empty, return `None`. If `k` exceeds the list length, return all the strings. If multiple strings have the same length, prioritize the earlier ones in the list.
"""

from typing import List, Optional

def longest(strings: List[str], k: int) -> Optional[List[str]]:
    if not strings:
        return None
   
    length_and_string = [(len(s), i, s) for i, s in enumerate(strings)]
    length_and_string.sort(key=lambda x: (-x[0], x[1]))
    longest_strings = [s for _, _, s in length_and_string[:k]]
    
    return longest_strings