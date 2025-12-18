"""
QUESTION:
Write a function `countConsecutiveChars` that takes a string `s` of lowercase English letters and returns a list of tuples, where each tuple contains a character and its consecutive count in the string. The function should run efficiently for large input strings.
"""

from typing import List, Tuple

def count_consecutive_chars(s: str) -> List[Tuple[str, int]]:
    if not s:
        return []

    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            result.append((s[i-1], count))
            count = 1
    result.append((s[-1], count))
    return result