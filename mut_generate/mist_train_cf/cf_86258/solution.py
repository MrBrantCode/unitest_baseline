"""
QUESTION:
Write a function `replace_and_count` that takes a string as input and returns a tuple containing the modified string with all occurrences of "o" (both uppercase and lowercase) replaced with "e", and the total count of "l" (both uppercase and lowercase) in the modified string. The function should work for strings of up to 10^5 characters in length.
"""

def replace_and_count(s):
    """
    Replaces all occurrences of 'o' (both uppercase and lowercase) with 'e' in the given string
    and returns a tuple containing the modified string and the total count of 'l' (both uppercase and lowercase).

    Args:
    s (str): The input string.

    Returns:
    tuple: A tuple containing the modified string and the count of 'l'.
    """
    modified_string = s.replace('o', 'e').replace('O', 'e')
    count = modified_string.lower().count('l')
    return modified_string, count