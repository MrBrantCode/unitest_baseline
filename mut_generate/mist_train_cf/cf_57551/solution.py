"""
QUESTION:
Write a function 'sorting_chars' that takes a list of strings as input and returns a list of these strings with their characters sorted alphabetically. If the list is empty, return 'None'. The function should handle strings containing special characters and numbers.
"""

from typing import List, Optional

def sorting_chars(strings: List[str]) -> Optional[List[str]]:
    if not strings:
        return None
    return [''.join(sorted(s)) for s in strings]