"""
QUESTION:
Write a function `is_rotation(s1, s2)` that takes two strings `s1` and `s2` as input and returns a boolean indicating whether `s2` is a rotation of `s1`. A string is considered a rotation of another if it can be obtained by rotating the characters of the other string. Assume that the input strings only contain lowercase letters and have the same length.
"""

def is_rotation(s1, s2):
    """
    Checks if s2 is a rotation of s1.

    Args:
    s1 (str): The original string.
    s2 (str): The string to be checked.

    Returns:
    bool: True if s2 is a rotation of s1, False otherwise.
    """
    if len(s1) != len(s2):
        return False
    return s2 in s1 + s1