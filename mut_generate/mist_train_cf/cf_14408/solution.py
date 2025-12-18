"""
QUESTION:
Write a recursive function `convert_string` that takes a string `s` as input and replaces all occurrences of 'c' with 'd'.
"""

def convert_string(s):
    """
    Recursively replaces all occurrences of 'c' with 'd' in a given string.

    Args:
    s (str): The input string.

    Returns:
    str: The modified string with all 'c's replaced with 'd's.
    """
    if not s:  # base case: empty string
        return ""
    if s[0] == 'c':  # if first character is 'c', replace it with 'd'
        return 'd' + convert_string(s[1:])
    return s[0] + convert_string(s[1:])  # recursive call for the rest of the string