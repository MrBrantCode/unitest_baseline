"""
QUESTION:
Implement a function `collapse_duplicates` that takes a string `s` as input and returns the same string with all consecutive duplicate characters collapsed into a single character. The function should not use any additional data structures like lists, dictionaries, or sets, and it should preserve the order of characters in the original string.

Function signature: `def collapse_duplicates(s: str) -> str`
"""

def collapse_duplicates(s: str) -> str:
    if not s:
        return s

    result = s[0]
    for char in s[1:]:
        if char != result[-1]:
            result += char

    return result