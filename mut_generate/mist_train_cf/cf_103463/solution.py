"""
QUESTION:
Create a function `get_substring(string, a, b)` that returns a substring of the input `string` from index `a` to `b` (inclusive). The function should handle edge cases where the string is empty, or `a` or `b` is negative, or `a` is greater than `b`, or `a` or `b` is out of the string's bounds. If `b` exceeds the string's length, it should be set to the last index of the string.
"""

def get_substring(string, a, b):
    """
    Returns a substring of the input string from index a to b (inclusive).
    
    Handles edge cases where the string is empty, or a or b is negative, 
    or a is greater than b, or a or b is out of the string's bounds. 
    If b exceeds the string's length, it is set to the last index of the string.

    Args:
        string (str): The input string.
        a (int): The start index of the substring.
        b (int): The end index of the substring.

    Returns:
        str: The substring of the input string from index a to b (inclusive).
    """

    if not string or a > b or a < 0 or b < 0:
        return ""
    if a >= len(string):
        return ""
    if b >= len(string):
        b = len(string) - 1
    
    return string[a:b+1]