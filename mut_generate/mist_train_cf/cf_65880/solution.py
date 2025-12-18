"""
QUESTION:
Create a function named 'longest_substring' that takes a list of strings and an integer 'k' as input and returns the longest common substring that appears at least 'k' times across the strings. If no such substring exists or the list is empty, return None. In case of a tie, return the substring which appears first in the list.
"""

from typing import List, Optional

def longest_substring(strings: List[str], k: int) -> Optional[str]:
    if len(strings) == 0:
        return None
    longest_str = ''
    for s in strings:
        for substr in (s[i: j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)):
            count = sum(substr in string for string in strings)
            if count >= k and len(substr) > len(longest_str):
                longest_str = substr
    return longest_str if longest_str != '' else None