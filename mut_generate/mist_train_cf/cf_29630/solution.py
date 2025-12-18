"""
QUESTION:
Write a function `valid_identifiers` that takes a list of strings as input and returns a new list containing only the strings that are valid Python identifiers. A valid Python identifier is a non-empty string consisting of only letters, digits, or underscores, and not starting with a digit. The function should handle the case where the input list is empty.
"""

from typing import List

def valid_identifiers(input_list: List[str]) -> List[str]:
    def is_valid_identifier(s: str) -> bool:
        if not s or s[0].isdigit():
            return False
        return all(c.isalnum() or c == '_' for c in s)

    return [s for s in input_list if is_valid_identifier(s)]