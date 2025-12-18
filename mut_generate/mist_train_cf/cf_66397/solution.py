"""
QUESTION:
Write a function called `replace_non_alphanumeric` that takes a string `s` and a replacement character as input, and returns the string where every unique non-alphanumeric character is replaced by the replacement character. The replacement character defaults to an underscore if not provided.
"""

def replace_non_alphanumeric(s: str, replacement="_") -> str:
    """
    This function takes a string s and a replacement character (default is underscore).
    It returns the string s where every unique non-alphanumeric character is replaced by the replacement character.
    """
    result = "".join([char if char.isalnum() else replacement for char in s])
    return result