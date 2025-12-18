"""
QUESTION:
Create a function `is_enclosed_by` that takes two parameters: `str` and `substring`. The function should return `True` if `str` is enclosed by `substring`, considering cases where overlap may occur, and `False` otherwise. The function should continue checking the remaining string by removing the first and last characters until the length of `str` is less than the length of `substring`.
"""

def is_enclosed_by(s, substring):
    """
    Checks if the string is enclosed by the given substring.

    Args:
        s (str): The input string.
        substring (str): The substring to check for.

    Returns:
        bool: True if the string is enclosed by the substring, False otherwise.
    """
    while len(s) >= len(substring):
        if s.startswith(substring) and s.endswith(substring):
            return True
        s = s[1:-1]
    return False