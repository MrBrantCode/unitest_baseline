"""
QUESTION:
Create a function called 'sorting_chars' that takes a list of strings as input. The function should return a string containing all words in the list sorted alphabetically, ignoring special characters and numbers. If the input is an empty list or contains only empty strings or strings with spaces, the function should return None.
"""

from typing import List, Optional

def sorting_chars(strings: List[str]) -> Optional[str]:
    if len(strings) == 0 or all([not s.strip() for s in strings]):
        return None
        
    final = []
    for s in strings:
        sorted_str = ''.join(sorted([ch for ch in s if ch.isalpha()]))
        final.append(sorted_str)
    return ' '.join(final)