"""
QUESTION:
Develop a function named `advanced_filter` that takes in a list of strings and a tuple containing a prefix, a suffix, an inner string, and a length. The function should return a list of strings that meet the following conditions:
- The string starts with the given prefix.
- The string ends with the specified suffix.
- The string contains the predetermined inner string.
- The string has a length greater than the specified length.
- The string has an odd number of characters.

The function should be recursive and able to handle empty input lists.
"""

from typing import List, Tuple

def advanced_filter(strings: List[str], prefix_suffix_inner_length: Tuple[str, str, str, int]) -> List[str]:
    """
    Filter an input list of strings only for ones that:
    - Start with a given prefix.
    - End with a specified suffix.
    - Contain a predetermined inner string.
    - Have a length greater than a specified length.
    - Have an odd number of characters.
    """
    prefix, suffix, inner, length = prefix_suffix_inner_length
    result = []

    def helper(s: str):
        if len(s) <= length or not s.startswith(prefix) or not s.endswith(suffix) or inner not in s or len(s) % 2 == 0:
            return
        result.append(s)
        helper(s[1:])

    for string in strings:
        helper(string)

    return result