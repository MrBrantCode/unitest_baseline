"""
QUESTION:
Implement a function named `count_unique_substring_strings` that takes two parameters: a substring and a list of strings. The function should return the count of unique strings that contain the specified substring, ignoring case sensitivity. If a string contains the substring multiple times, it should only be counted once. If the input list is empty or no strings contain the specified substring, the function should return 0.
"""

from typing import List

def count_unique_substring_strings(substring: str, strings: List[str]) -> int:
    substring_lower = substring.lower()
    unique_strings = set()
    for s in strings:
        s_lower = s.lower()
        if substring_lower in s_lower:
            unique_strings.add(s_lower)
    return len(unique_strings)