"""
QUESTION:
Write a function `to_lower(s)` that takes a string `s` as input and returns a tuple containing the string with all letters converted to lowercase and the count of uppercase letters encountered in the string. The function should not use any built-in case changing functions such as `lower()`.
"""

def to_lower(s):
    """
    This function takes a string as input, converts all letters to lowercase, 
    and returns a tuple containing the resulting string and the count of 
    uppercase letters encountered.

    Args:
        s (str): The input string.

    Returns:
        tuple: A tuple containing the string with all letters converted to 
        lowercase and the count of uppercase letters.
    """
    lower_str = ""
    count_upper = 0
    for c in s:
        if 'A' <= c <= 'Z':
            count_upper += 1
            lower_str += chr(ord(c) + 32)
        else:
            lower_str += c
    return lower_str, count_upper