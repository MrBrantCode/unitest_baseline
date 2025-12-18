"""
QUESTION:
Create a function called `has_suffix` that takes two parameters: a string `str` and a substring `suffix`. The function should return `True` if the string `str` ends with the substring `suffix`, regardless of how many times `suffix` occurs at the end, and `False` otherwise.
"""

def has_suffix(str, suffix):
    """
    Checks if the input string `str` ends with the substring `suffix`.
    
    Args:
        str (str): The input string.
        suffix (str): The substring to check.
    
    Returns:
        bool: True if `str` ends with `suffix`, False otherwise.
    """
    if len(suffix) > len(str):
        return False

    for i in range(len(suffix)):
        if str[len(str) - i - 1] != suffix[len(suffix) - i - 1]:
            return False

    return True