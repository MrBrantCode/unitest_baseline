"""
QUESTION:
Write a function named `is_substring` that takes two strings as inputs and returns True if one string is a substring of the other, and False otherwise. The function should only consider strings that are non-empty and contain only alphabetical characters, and it should be case-insensitive. If the two strings are identical, the function should return False. Additionally, the function should be able to handle multiple pairs of input strings.
"""

def is_substring(s1, s2):
    """
    Checks if one string is a substring of the other, subject to the following conditions:
    - Both strings are non-empty.
    - Both strings contain only alphabetical characters.
    - The comparison is case-insensitive.
    - If the two strings are identical, the function returns False.

    Args:
        s1 (str): The first string.
        s2 (str): The second string.

    Returns:
        bool: True if one string is a substring of the other, False otherwise.
    """
    if not s1.isalpha() or not s2.isalpha() or not s1 or not s2:
        return False
    s1 = s1.lower()
    s2 = s2.lower()
    if s1 == s2:
        return False
    return s1 in s2 or s2 in s1