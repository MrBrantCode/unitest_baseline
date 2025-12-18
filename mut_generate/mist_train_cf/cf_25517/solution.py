"""
QUESTION:
Create a function `canBeEqual(s1, s2)` that takes two strings `s1` and `s2` as input and returns a boolean indicating whether `s1` can be transformed into `s2` by replacing some characters in `s1` with asterisks (*) in the same order. The function should return `false` if the lengths of `s1` and `s2` are different, or if there exists a character in `s2` that is not an asterisk and does not match the corresponding character in `s1`.
"""

def canBeEqual(s1: str, s2: str) -> bool:
    """
    Checks if s1 can be transformed into s2 by replacing some characters in s1 with asterisks (*) in the same order.

    Args:
    s1 (str): The original string.
    s2 (str): The target string.

    Returns:
    bool: True if s1 can be transformed into s2, False otherwise.
    """

    if len(s1) != len(s2): 
        return False
    for c1, c2 in zip(s1, s2):
        if c1 != c2 and c2 != '*': 
            return False
    return True